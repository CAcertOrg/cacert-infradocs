# -*- python -*-
# This module provides the following CAcert specific sphinx directives
#
# sslcert
# sslcertlist
# sshkeys
# sshkeylist

import re
import os.path
from ipaddress import ip_address

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.errors import SphinxError
from sphinx.util.nodes import set_source_info, make_refnode, traverse_parent

from dateutil.parser import parse as date_parse
from validate_email import validate_email

__version__ = '0.1.0'

SUPPORTED_SSH_KEYTYPES = ('RSA', 'DSA', 'ECDSA', 'ED25519')


class sslcert_node(nodes.General, nodes.Element):
    pass


class sslcertlist_node(nodes.General, nodes.Element):
    pass


class sshkeys_node(nodes.General, nodes.Element):
    pass


class sshkeylist_node(nodes.General, nodes.Element):
    pass


# mapping and validation functions for directive options

def hex_int(argument):
    value = int(argument, base=16)
    return value


def md5_fingerprint(argument):
    value = argument.strip().lower()
    if not re.match(r'^([0-9a-f]{2}:){15}[0-9a-f]{2}$', value):
        raise ValueError('no correctly formatted SHA1 fingerprint')
    return value


def sha1_fingerprint(argument):
    value = argument.strip().lower()
    if not re.match(r'^([0-9a-f]{2}:){19}[0-9a-f]{2}$', value):
        raise ValueError('no correctly formatted SHA1 fingerprint')
    return value


def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":  # strip exactly one dot from the right, if present
        hostname = hostname[:-1]
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))


def is_valid_ipaddress(content):
    try:
        ip_address(content)
    except ValueError:
        return False
    return True


def subject_alternative_names(argument):
    value = [san.strip().split(':', 1) for san in argument.split(',')]
    for typ, content in value:
        if typ == 'DNS':
            if not is_valid_hostname(content):
                raise ValueError("%s is no valid DNS name" % content)
        elif typ == 'EMAIL':
            if not validate_email(content):
                raise ValueError("%s is not a valid email address" % content)
        elif typ == 'IP':
            if not is_valid_ipaddress(content):
                raise ValueError("%s is not a valid IP address" % content)
        else:
            raise ValueError(
                "handling of %s subject alternative names (%s) has not been "
                "implemented" % (typ, content))
    return value


def expiration_date(argument):
    return date_parse(directives.unchanged_required(argument))


class CAcertSSLCert(Directive):
    """
    The sslcert directive implementation.

    There must only be one instance of a certificate with the same CN and
    serial number that is not flagged as secondary
    """
    final_argument_whitespace = True
    required_arguments = 1
    option_spec = {
        'certfile': directives.path,
        'keyfile': directives.path,
        'serial': hex_int,
        'expiration': expiration_date,
        'sha1fp': sha1_fingerprint,
        'altnames': subject_alternative_names,
        'issuer': directives.unchanged_required,
        'secondary': directives.flag
    }

    def run(self):
        if 'secondary' in self.options:
            missing = [
                required for required in ('certfile', 'keyfile', 'serial')
                if required not in self.options
            ]
        else:
            missing = [
                required for required in (
                    'certfile', 'keyfile', 'serial', 'expiration', 'sha1fp',
                    'issuer')
                if required not in self.options
            ]
        if missing:
            raise self.error(
                "required option(s) '%s' is/are not set for %s." % (
                    "', '".join(missing), self.name))
        sslcert = sslcert_node()
        sslcert.attributes['certdata'] = self.options.copy()
        sslcert.attributes['certdata']['cn'] = self.arguments[0]
        set_source_info(self, sslcert)

        env = self.state.document.settings.env
        targetid = 'sslcert-%s' % env.new_serialno('sslcert')
        targetnode = nodes.target('', '', ids=[targetid])
        para = nodes.paragraph()
        para.append(targetnode)
        para.append(sslcert)
        return [para]


class CAcertSSLCertList(Directive):
    """
    The sslcertlist directive implementation
    """
    def run(self):
        return [sslcertlist_node()]


class CAcertSSHKeys(Directive):
    """
    The sshkeys directive implementation that can be used to specify the ssh
    host keys for a host.
    """
    option_spec = {
        keytype.lower(): md5_fingerprint for keytype in SUPPORTED_SSH_KEYTYPES
    }
    def run(self):
        if len(self.options) == 0:
            raise self.error(
                "at least one ssh key fingerprint must be specified. The "
                "following formats are supported: %s" % ", ".join(
                    SUPPORTED_SSH_KEYTYPES))
        sshkeys = sshkeys_node()
        sshkeys.attributes['keys'] = self.options.copy()
        set_source_info(self, sshkeys)

        env = self.state.document.settings.env
        secid = 'sshkeys-%s' % env.new_serialno('sshkeys')

        section = nodes.section(ids=[secid])
        section += nodes.title(text='SSH host keys')
        section += sshkeys
        return [section]


class CAcertSSHKeyList(Directive):
    """
    The sshkeylist directive implementation
    """
    def run(self):
        return [sshkeylist_node()]


def create_table_row(rowdata):
    row = nodes.row()
    for cell in rowdata:
        entry = nodes.entry()
        row += entry
        entry += cell
    return row


def _sslcert_item_key(item):
    return "%s-%d" % (item['cn'], item['serial'])


def _sshkeys_item_key(item):
    return "%s" % os.path.basename(item['docname'])


def _build_cert_anchor_name(cn, serial):
    return 'cert_%s_%d' % (cn.replace('.', '_'), serial)


def _format_subject_alternative_names(altnames):
    return nodes.paragraph(text=", ".join(
        [content for _, content in altnames]
    ))


def _place_sort_key(place):
    return "%s-%d" % (place['docname'], place['lineno'])


def _file_ref_paragraph(cert_info, filekey, app, env, docname):
    para = nodes.paragraph()

    places = [place for place in cert_info['places'] if place['primary']]
    places.extend(sorted([
        place for place in cert_info['places'] if not place['primary']],
        key=_place_sort_key))

    for pos in range(len(places)):
        place = places[pos]
        title = env.titles[place['docname']].astext().lower()
        if place['primary'] and len(places) > 1:
            reftext = nodes.strong(text=title)
        else:
            reftext = nodes.Text(title)
        para += make_refnode(
            app.builder, docname, place['docname'], place['target']['ids'][0],
            reftext)
        para += nodes.Text(":")
        para += addnodes.literal_emphasis(text=place[filekey])
        if pos + 1 < len(places):
            para += nodes.Text(", ")
    return para


def _format_serial_number(serial):
    return nodes.paragraph(text="%d (0x%0x)" % (serial, serial))


def _format_expiration_date(expiration):
    return nodes.paragraph(text=expiration)


def _format_fingerprint(fingerprint):
    para = nodes.paragraph()
    para += nodes.literal(text=fingerprint, classes=['fingerprint'])
    return para


def _get_cert_index_text(cert_info):
    return "Certificate; %s" % cert_info['cn']


def _get_formatted_keyentry(keys_info, algorithm):
    entry = nodes.entry()
    algkey = algorithm.lower()
    if algkey in keys_info:
        para = nodes.paragraph()
        keyfp = nodes.literal(text=keys_info[algkey])
        para += keyfp
    else:
        para = nodes.paragraph(text="-")
    entry += para
    return entry


def process_sslcerts(app, doctree):
    env = app.builder.env
    if not hasattr(env, 'cacert_sslcerts'):
        env.cacert_sslcerts = []

    for node in doctree.traverse(sslcertlist_node):
        if hasattr(env, 'cacert_certlistdoc'):
            raise SphinxError(
                "There must be one sslcertlist directive present in "
                "the document tree only.")
        env.cacert_certlistdoc = env.docname

    for node in doctree.traverse(sslcert_node):
        try:
            targetnode = node.parent[node.parent.index(node) - 1]
            if not isinstance(targetnode, nodes.target):
                raise IndexError
        except IndexError:
            targetnode = None
        certdata = node.attributes['certdata'].copy()
        existing = [
            cert_info for cert_info in env.cacert_sslcerts
            if (cert_info['cn'], cert_info['serial']) ==
               (certdata['cn'], certdata['serial'])
        ]
        place_info = {
            'docname': env.docname,
            'lineno': node.line,
            'certfile': certdata['certfile'],
            'keyfile': certdata['keyfile'],
            'primary': 'secondary' not in certdata,
            'target': targetnode,
        }
        if existing:
            info = existing[0]
        else:
            info = {
                'cn': certdata['cn'],
                'serial': certdata['serial'],
                'places': [],
            }
            env.cacert_sslcerts.append(info)
        info['places'].append(place_info)
        if 'sha1fp' in certdata:
            info['sha1fp'] = certdata['sha1fp']
        if 'issuer' in certdata:
            info['issuer'] = certdata['issuer']
        if 'expiration' in certdata:
            info['expiration'] = certdata['expiration']
        if 'altnames' in certdata:
            info['altnames'] = certdata['altnames'].copy()
        indexnode = addnodes.index(entries=[
            ('pair', _get_cert_index_text(info), targetnode['ids'][0],
             '', None)
        ])

        bullets = nodes.bullet_list()
        certitem = nodes.list_item()
        bullets += certitem
        certpara = nodes.paragraph()
        certpara += nodes.Text('Certificate for CN %s, see ' % certdata['cn'])
        refid = _build_cert_anchor_name(certdata['cn'], certdata['serial'])
        detailref = addnodes.pending_xref(
            reftype='certlistref', refdoc=env.docname, refid=refid,
            reftarget='certlist'
        )
        detailref += nodes.Text("details in the certificate list")
        certpara += detailref
        certitem += certpara

        subbullets = nodes.bullet_list()
        bullets += subbullets
        item = nodes.list_item()
        subbullets += item
        certfile = nodes.paragraph(text="certificate in file ")
        certfile += addnodes.literal_emphasis(text=certdata['certfile']) #, node.line)
        item += certfile
        item = nodes.list_item()
        subbullets += item
        keyfile = nodes.paragraph(text="private key in file ")
        keyfile += addnodes.literal_emphasis(text=certdata['keyfile'])
        #keyfile += _create_interpreted_file_node(
        #    certdata['keyfile'], node.line)
        item += keyfile

        node.parent.replace_self([targetnode, indexnode, bullets])
        #env.note_indexentries_from(env.docname, doctree)


def process_sshkeys(app, doctree):
    env = app.builder.env
    if not hasattr(env, 'cacert_sshkeys'):
        env.cacert_sshkeys = []

    for _ in doctree.traverse(sshkeylist_node):
        if hasattr(env, 'cacert_sshkeylistdoc'):
            raise SphinxError(
                "There must be one sshkeylist directive present in "
                "the document tree only.")
        env.cacert_sshkeylistdoc = env.docname

    for node in doctree.traverse(sshkeys_node):
        # find section
        section = [s for s in traverse_parent(node, nodes.section)][0]
        dockeys = {'docname': env.docname, 'secid': section['ids'][0]}
        dockeys.update(node['keys'])
        env.cacert_sshkeys.append(dockeys)

        secparent = section.parent
        pos = secparent.index(section)
        # add index node for section
        indextitle = 'SSH host key; %s' % (
            env.docname in env.titles and env.titles[env.docname].astext()
            or os.path.basename(env.docname)
        )
        secparent.insert(pos, addnodes.index(entries=[
            ('pair', indextitle, section['ids'][0], '', None),
        ]))

        # add table
        content = []
        table = nodes.table()
        content.append(table)
        cols = (1, 4)
        tgroup = nodes.tgroup(cols=len(cols))
        table += tgroup
        for col in cols:
            tgroup += nodes.colspec(colwidth=col)
        thead = nodes.thead()
        tgroup += thead
        thead += create_table_row([
            nodes.paragraph(text='Algorithm'),
            nodes.paragraph(text='Fingerprint'),
        ])
        tbody = nodes.tbody()
        tgroup += tbody
        for alg in SUPPORTED_SSH_KEYTYPES:
            if alg.lower() in dockeys:
                fpparagraph = nodes.paragraph()
                fpparagraph += nodes.literal(text=dockeys[alg.lower()])
            else:
                fpparagraph = nodes.paragraph(text='-')
            tbody += create_table_row([
                nodes.paragraph(text=alg),
                fpparagraph,
            ])
        # add pending_xref for link to ssh key list
        seealso = addnodes.seealso()
        content.append(seealso)
        detailref = addnodes.pending_xref(
            reftype='sshkeyref', refdoc=env.docname, refid='sshkeylist',
            reftarget='sshkeylist'
        )
        detailref += nodes.Text("SSH host key list")
        seepara = nodes.paragraph()
        seepara += detailref
        seealso += seepara

        node.replace_self(content)


def process_sslcert_nodes(app, doctree, docname):
    env = app.builder.env

    if not hasattr(env, 'cacert_sslcerts'):
        env.cacert_sslcerts = []

    for node in doctree.traverse(sslcertlist_node):
        content = []

        for cert_info in sorted(env.cacert_sslcerts, key=_sslcert_item_key):
            primarycount = len([
                place for place in cert_info['places'] if place['primary']
            ])
            if primarycount != 1:
                raise SphinxError(
                    "There must be exactly one primary place for a "
                    "certificate, but the certificate for CN %s with "
                    "serial number %d has %d" %
                    (cert_info['cn'], cert_info['serial'], primarycount)
                )
            cert_sec = nodes.section()
            cert_sec['ids'].append(
                _build_cert_anchor_name(cert_info['cn'],
                                        cert_info['serial'])
            )
            cert_sec += nodes.title(text=cert_info['cn'])
            indexnode = addnodes.index(entries=[
                ('pair', _get_cert_index_text(cert_info),
                 cert_sec['ids'][0], '', None),
            ])
            content.append(indexnode)
            table = nodes.table()
            cert_sec += table
            tgroup = nodes.tgroup(cols=2)
            table += tgroup
            tgroup += nodes.colspec(colwidth=1)
            tgroup += nodes.colspec(colwidth=5)
            tbody = nodes.tbody()
            tgroup += tbody
            tbody += create_table_row([
                nodes.paragraph(text='Common Name'),
                nodes.paragraph(text=cert_info['cn'])
            ])
            if 'altnames' in cert_info:
                tbody += create_table_row([
                    nodes.paragraph(text='Subject Alternative Names'),
                    _format_subject_alternative_names(
                        cert_info['altnames'])
                ])
            tbody += create_table_row([
                nodes.paragraph(text='Key kept at'),
                _file_ref_paragraph(cert_info, 'keyfile', app, env, docname)
            ])
            tbody += create_table_row([
                nodes.paragraph(text='Cert kept at'),
                _file_ref_paragraph(cert_info, 'certfile', app, env, docname)
            ])
            tbody += create_table_row([
                nodes.paragraph(text='Serial number'),
                _format_serial_number(cert_info['serial'])
            ])
            tbody += create_table_row([
                nodes.paragraph(text='Expiration date'),
                _format_expiration_date(cert_info['expiration'])
            ])
            tbody += create_table_row([
                nodes.paragraph(text='Issuer'),
                nodes.paragraph(text=cert_info['issuer'])
            ])
            tbody += create_table_row([
                nodes.paragraph(text='SHA1 fingerprint'),
                _format_fingerprint(cert_info['sha1fp'])
            ])
            content.append(cert_sec)

        node.replace_self(content)
        #env.note_indexentries_from(docname, doctree)


def process_sshkeys_nodes(app, doctree, docname):
    env = app.builder.env

    if not hasattr(env, 'cacert_sshkeys'):
        env.cacert_sslcerts = []

    for node in doctree.traverse(sshkeylist_node):
        content = []
        content.append(nodes.target(ids=['sshkeylist']))

        if len(env.cacert_sshkeys) > 0:
            table = nodes.table()
            content.append(table)
            tgroup = nodes.tgroup(cols=3)
            tgroup += nodes.colspec(colwidth=1)
            tgroup += nodes.colspec(colwidth=1)
            tgroup += nodes.colspec(colwidth=4)
            table += tgroup

            thead = nodes.thead()
            row = nodes.row()
            entry = nodes.entry()
            entry += nodes.paragraph(text="Host")
            row += entry
            entry = nodes.entry(morecols=1)
            entry += nodes.paragraph(text="SSH Host Keys")
            row += entry
            thead += row
            tgroup += thead

            tbody = nodes.tbody()
            tgroup += tbody

            for keys_info in sorted(env.cacert_sshkeys, key=_sshkeys_item_key):
                trow = nodes.row()
                entry = nodes.entry(morerows=len(SUPPORTED_SSH_KEYTYPES))
                para = nodes.paragraph()
                para += make_refnode(
                    app.builder, docname, keys_info['docname'],
                    keys_info['secid'],
                    nodes.Text(env.titles[keys_info['docname']].astext())
                )
                entry += para
                trow += entry

                entry = nodes.entry()
                para = nodes.paragraph()
                para += nodes.strong(text='Algorithm')
                entry += para
                trow += entry

                entry = nodes.entry()
                para = nodes.paragraph()
                para += nodes.strong(text='SSH host key MD5 fingerprint')
                entry += para
                trow += entry

                tbody += trow

                for algorithm in SUPPORTED_SSH_KEYTYPES:
                    trow = nodes.row()

                    entry = nodes.entry()
                    entry += nodes.paragraph(text=algorithm)
                    trow += entry

                    trow += _get_formatted_keyentry(keys_info, algorithm)
                    tbody += trow
        else:
            content.append(nodes.paragraph(
                text="No ssh keys have been documented.")
            )

        node.replace_self(content)


def resolve_missing_reference(app, env, node, contnode):
    if node['reftype'] == 'certlistref':
        if hasattr(env, 'cacert_certlistdoc'):
            return make_refnode(
                app.builder, node['refdoc'], env.cacert_certlistdoc,
                node['refid'], contnode)
        raise SphinxError('No certlist directive found in the document tree')
    if node['reftype'] == 'sshkeyref' :
        if hasattr(env, 'cacert_sshkeylistdoc'):
            return make_refnode(
                app.builder, node['refdoc'], env.cacert_sshkeylistdoc,
                node['refid'], contnode)
        raise SphinxError('No sshkeylist directive found in the document tree')


def purge_sslcerts(app, env, docname):
    if (
        hasattr(env, 'cacert_certlistdoc') and
        env.cacert_certlistdoc == docname
    ):
        delattr(env, 'cacert_certlistdoc')
    if not hasattr(env, 'cacert_sslcerts'):
        return
    for cert_info in env.cacert_sslcerts:
        cert_info['places'] = [
            place for place in cert_info['places']
            if place['docname'] != docname
        ]


def purge_sshkeys(app, env, docname):
    if (
        hasattr(env, 'cacert_sshkeylistdoc') and
        env.cacert_sshkeylistdoc == docname
    ):
        delattr(env, 'cacert_sshkeylistdoc')
    if not hasattr(env, 'cacert_sshkeys'):
        return
    env.cacert_sshkeys = [
        keys for keys in env.cacert_sshkeys if keys['docname'] != docname
    ]


def setup(app):
    app.add_node(sslcertlist_node)
    app.add_node(sslcert_node)
    app.add_node(sshkeylist_node)
    app.add_node(sshkeys_node)

    app.add_directive('sslcert', CAcertSSLCert)
    app.add_directive('sslcertlist', CAcertSSLCertList)
    app.add_directive('sshkeys', CAcertSSHKeys)
    app.add_directive('sshkeylist', CAcertSSHKeyList)

    app.connect('doctree-read', process_sslcerts)
    app.connect('doctree-read', process_sshkeys)
    app.connect('doctree-resolved', process_sslcert_nodes)
    app.connect('doctree-resolved', process_sshkeys_nodes)
    app.connect('missing-reference', resolve_missing_reference)
    app.connect('env-purge-doc', purge_sslcerts)
    app.connect('env-purge-doc', purge_sshkeys)
    return {'version': __version__}
