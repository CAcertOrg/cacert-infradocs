#!/usr/bin/env python

from __future__ import print_function

from datetime import datetime
from hashlib import sha1
import argparse
import os.path

from pyasn1_modules import pem
from pyx509.pkcs7.asn1_models.X509_certificate import Certificate
from pyx509.pkcs7_models import X509Certificate
from pyx509.pkcs7.asn1_models.decoder_workarounds import decode


ALTNAME_MAP = (
    ('dNSName', 'DNS'),
    ('rfc822Name', 'EMAIL'),
    ('iPAddress', 'IP')
)


def x509_parse(derData):
    """Decodes certificate.
    @param derData: DER-encoded certificate string
    @returns: pkcs7_models.X509Certificate
    """
    cert = decode(derData, asn1Spec=Certificate())[0]
    x509cert = X509Certificate(cert)
    return x509cert


def get_altnames(cert):
    altnames = cert.tbsCertificate.subjAltNameExt.value.values
    retval = []
    for typ, data in [(field[1], altnames[field[0]]) for field in ALTNAME_MAP]:
        for item in sorted(data):
            retval.append("{typ}:{item}".format(typ=typ, item=item))
    return ", ".join(retval)


def get_serial(cert):
    serial = "%X" % cert.tbsCertificate.serial_number
    return "0" * (len(serial) % 2) + serial


def get_expiration(cert):
    return datetime.strptime(
        cert.tbsCertificate.validity.valid_to, '%Y%m%d%H%M%SZ'
    ).strftime('%b %d %H:%M:%S %y GMT')


def get_sha1fp(certdata):
    hexhash = sha1(certdata).hexdigest().upper()
    return ":".join([hexhash[i:i+2] for i in range(0, len(hexhash), 2)])


def get_issuer(cert):
    return cert.tbsCertificate.issuer.get_attributes()['CN'][0]


def get_subject(cert):
    return cert.tbsCertificate.subject.get_attributes()['CN'][0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            'Create an sslcert directive from data taken from a PEM encoded '
            'X.509 certificate file and its corresponding PEM encoded RSA key '
            'file.'))
    parser.add_argument(
        'cert', metavar='CERT', type=open,
        help='PEM encoded X.509 certficate file')
    parser.add_argument(
        '--key', metavar='KEY', type=open,
        help='PEM encoded RSA private key', default=None)
    parser.add_argument(
        '--root', metavar='ROOT', type=str,
        help='Relative root directory for key and cert')

    args = parser.parse_args()

    certpem = pem.readPemFromFile(args.cert)
    certpath = os.path.abspath(args.cert.name)
    if args.root:
        certpath = '/' + os.path.relpath(certpath, args.root)
    if args.key:
        haskey = True
        keypem = pem.readPemFromFile(args.key)
        keypath = os.path.abspath(args.key.name)
        if args.root:
            keypath = '/' + os.path.relpath(keypath, args.root)
    else:
        keypath = 'TODO: define key path'

    cert = x509_parse(certpem)
    data = {
        'altnames': get_altnames(cert),
        'certfile': certpath,
        'keyfile': keypath,
        'serial': get_serial(cert),
        'expiration': get_expiration(cert),
        'sha1fp': get_sha1fp(certpem),
        'issuer': get_issuer(cert),
        'subject': get_subject(cert),
    }
    print(""".. sslcert:: {subject}
   :altnames:   {altnames}
   :certfile:   {certfile}
   :keyfile:    {keyfile}
   :serial:     {serial}
   :expiration: {expiration}
   :sha1fp:     {sha1fp}
   :issuer:     {issuer}
""".format(**data))
