#!/usr/bin/env python

from glob import glob
import argparse
import os.path
import subprocess


SUPPORTED_SSH_KEYTYPES = ('RSA', 'DSA', 'ECDSA', 'ED25519')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            'Convert a set of ssh host keys to the syntax expected by the '
            'sshkeys directive of the CAcert infrastructur documentation'))
    parser.add_argument(
        'root', metavar='ROOT', type=str, help='root directory'
    )
    args = parser.parse_args()

    keys = {}
    for host_key in glob(os.path.join(
        args.root, 'etc/ssh', 'ssh_host_*key.pub')
    ):
        fp = subprocess.check_output(
            ['ssh-keygen', '-l', '-f', host_key]).strip().split()
        keys[fp[3][1:-1]] = fp[1]

    maxlen = max([len(key) for key in keys.keys() if key in SUPPORTED_SSH_KEYTYPES])

    print ".. sshkeys::"
    for typ, key in [
        (typ, keys[typ]) for typ in SUPPORTED_SSH_KEYTYPES
        if typ in keys
    ]:
        print "   :%s:%s %s" % (typ, ' ' * (maxlen - len(typ)), key)
