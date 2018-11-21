#!/usr/bin/env python3

from __future__ import print_function

import argparse
import os.path
from hashlib import sha1

from asn1crypto import pem
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import ExtensionOID, NameOID

ALTNAME_MAP = (
    (x509.DNSName, 'DNS'),
    (x509.RFC822Name, 'EMAIL'),
    (x509.IPAddress, 'IP')
)


def get_altnames(cert):
    altnames = cert.extensions.get_extension_for_oid(
        ExtensionOID.SUBJECT_ALTERNATIVE_NAME)

    retval = []
    for altname_type, field_name in ALTNAME_MAP:
        names = altnames.value.get_values_for_type(altname_type)
        for item in sorted(names):
            retval.append("{typ}:{item}".format(typ=field_name, item=item))
    return ", ".join(retval)


def get_serial(cert):
    serial = "%X" % cert.serial_number
    return "0" * (len(serial) % 2) + serial


def get_expiration(cert):
    return cert.not_valid_after.strftime('%b %d %H:%M:%S %Y GMT')


def get_sha1fp(pem_data):
    cert_data = pem.unarmor(pem_data)
    hex_hash = sha1(cert_data[2]).hexdigest().upper()
    return ":".join([hex_hash[i:i + 2] for i in range(0, len(hex_hash), 2)])


def get_issuer(cert):
    return cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value


def get_subject(cert):
    return cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            'Create an sslcert directive from data taken from a PEM encoded '
            'X.509 certificate file and its corresponding PEM encoded RSA key '
            'file.'))
    parser.add_argument(
        'cert', metavar='CERT', type=argparse.FileType('rb'),
        help='PEM encoded X.509 certificate file')
    parser.add_argument(
        '--key', metavar='KEY', type=argparse.FileType('rb'),
        help='PEM encoded RSA private key', default=None)
    parser.add_argument(
        '--root', metavar='ROOT', type=str,
        help='Relative root directory for key and cert')

    args = parser.parse_args()

    cert_path = os.path.abspath(args.cert.name)
    if args.root:
        cert_path = '/' + os.path.relpath(cert_path, args.root)
    if args.key:
        has_key = True
        key_path = os.path.abspath(args.key.name)
        if args.root:
            key_path = '/' + os.path.relpath(key_path, args.root)
    else:
        key_path = 'TODO: define key path'

    cert_pem = args.cert.read()
    certificate = x509.load_pem_x509_certificate(cert_pem, default_backend())
    data = {
        'altnames': get_altnames(certificate),
        'certfile': cert_path,
        'keyfile': key_path,
        'serial': get_serial(certificate),
        'expiration': get_expiration(certificate),
        'sha1fp': get_sha1fp(cert_pem),
        'issuer': get_issuer(certificate),
        'subject': get_subject(certificate),
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
