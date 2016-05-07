# -*- python -*-
# This module provides the following CAcert specific sphinx directives
#
# sslcert
# sslcertlist
# sshkeys
# sshkeylist

__version__ = '0.1.0'

import re

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils.parsers.rst import roles

from sphinx import addnodes
from sphinx.errors import SphinxError
from sphinx.util.nodes import set_source_info, make_refnode


class sslcert_node(nodes.General, nodes.Element):
    pass


class sslcertlist_node(nodes.General, nodes.Element):
    pass


def hex_int(argument):
    value = int(argument, base=16)
    return value


def sha1_fingerprint(argument):
    value = argument.strip().lower()
    if not re.match(r'^([0-9a-f]{2}:){19}[0-9a-f]{2}$', value):
        raise ValueError('no correctly formatted SHA1 fingerprint')
    return value


def create_table_row(rowdata):
    row = nodes.row()
    for cell in rowdata:
        entry = nodes.entry()
        row += entry
        entry += cell
    return row


def subject_alternative_names(argument):
    value = [san.strip() for san in argument.split(',')]
    # TODO: sanity checks for SANs
    return value


def expiration_date(argument):
    # TODO: normalize to internal format
    return directives.unchanged_required(argument)


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
    def run(self):
        return []

class CAcertSSHKeyList(Directive):
    """
    The sshkeylist directive implementation
    """
    def run(self):
        return []


def _create_interpreted_file_node(text, line=0):
    return roles._roles['file']('', ':file:`%s`' % text,
                                text, line, None)[0][0]


def process_sslcerts(app, doctree):
    env = app.builder.env
    if not hasattr(env, 'cacert_sslcerts'):
        env.cacert_sslcerts = []

    for node in doctree.traverse(sslcertlist_node):
        if hasattr(env, 'cacert_certlistdoc'):
            raise SphinxError(
                "There must only be one sslcertlist directive present in "
                "the document tree.")
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
            ('single', _get_cert_index_text(info), targetnode['ids'][0],
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
        certfile += _create_interpreted_file_node(
            certdata['certfile'], node.line)
        item += certfile
        item = nodes.list_item()
        subbullets += item
        keyfile = nodes.paragraph(text="private key in file ")
        keyfile += _create_interpreted_file_node(
            certdata['keyfile'], node.line)
        item += keyfile

        node.parent.replace_self([targetnode, indexnode, bullets])
        env.note_indexentries_from(env.docname, doctree)


def _sslcert_item_key(item):
    return "%s-%d" % (item['cn'], item['serial'])


def _build_cert_anchor_name(cn, serial):
    return 'cert_%s_%d' % (cn.replace('.', '_'), serial)


def _format_subject_alternative_names(altnames):
    return nodes.paragraph(text = ", ".join(altnames))


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
        para += _create_interpreted_file_node(place[filekey])
        if pos + 1 < len(places):
            para += nodes.Text(", ")
    return para


def _format_serial_number(serial):
    return nodes.paragraph(text="%d (0x%0x)" % (serial, serial))


def _format_expiration_date(expiration):
    # TODO use a normalized date format
    return nodes.paragraph(text=expiration)


def _format_fingerprint(fingerprint):
    para = nodes.paragraph()
    para += nodes.literal(text=fingerprint, classes=['fingerprint'])
    return para


def _get_cert_index_text(cert_info):
    return "Certificate; %s" % cert_info['cn']


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
                ('single', _get_cert_index_text(cert_info),
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
        env.note_indexentries_from(docname, doctree)


def resolve_missing_reference(app, env, node, contnode):
    if not hasattr(env, 'cacert_certlistdoc'):
        return
    if node['reftype'] == 'certlistref':
        return make_refnode(
            app.builder, node['refdoc'], env.cacert_certlistdoc,
            node['refid'], contnode)


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


def setup(app):
    app.add_node(sslcertlist_node)
    app.add_node(sslcert_node)

    app.add_directive('sslcert', CAcertSSLCert)
    app.add_directive('sslcertlist', CAcertSSLCertList)
    app.add_directive('sshkeys', CAcertSSHKeys)
    app.add_directive('sshkeylist', CAcertSSHKeyList)

    app.connect('doctree-read', process_sslcerts)
    app.connect('doctree-resolved', process_sslcert_nodes)
    app.connect('missing-reference', resolve_missing_reference)
    app.connect('env-purge-doc', purge_sslcerts)
    return {'version': __version__}
