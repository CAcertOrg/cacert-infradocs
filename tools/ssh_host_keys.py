#!/usr/bin/env python3

import argparse
import os.path
import subprocess
from glob import glob

SUPPORTED_SSH_KEY_TYPES = ("RSA", "DSA", "ECDSA", "ED25519")
HASH_ALGORITHMS = ("SHA256", "MD5")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Convert a set of ssh host keys to the syntax expected by the "
            "sshkeys directive of the CAcert infrastructure documentation"
        )
    )
    parser.add_argument("root", metavar="ROOT", type=str, help="root directory")
    args = parser.parse_args()

    keys = {}
    for host_key in glob(os.path.join(args.root, "etc/ssh", "ssh_host_*key.pub")):
        for algorithm in HASH_ALGORITHMS:
            fp = (
                subprocess.check_output(
                    ["ssh-keygen", "-l", "-E", algorithm, "-f", host_key]
                )
                .decode("ascii")
                .strip()
                .split()
            )
            key_type = fp[3][1:-1]
            keys.setdefault(key_type, {})
            keys[key_type][algorithm] = fp[1]

    max_length = max(
        [len(key) for key in keys.keys() if key in SUPPORTED_SSH_KEY_TYPES]
    )

    print(".. sshkeys::")
    for typ, key_dict in [
        (typ, keys[typ]) for typ in SUPPORTED_SSH_KEY_TYPES if typ in keys
    ]:
        print(
            "   :{}:{} {}".format(
                typ,
                " " * (max_length - len(typ)),
                " ".join([key_dict[algorithm] for algorithm in HASH_ALGORITHMS]),
            )
        )
