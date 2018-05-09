"""QInt Data Encoder v0.1"""
import base64
import argparse

superstrongkey = "password1"
n = 13


def encode(key, string):
    """Function to encode secret client data using key."""
    abc = "abcdefghijklmnopqrstuvwxyz" * 2
    abc = abc + abc.upper()
    def get_i():
        for i in range(26):
            yield i
        for i in range(53, 78):
            yield i
    step1 = {abc[i]: abc[i+n] for i in get_i()}
    step2 = "".join(step1.get(i,i) for i in string)

    enc = []
    for i in range(len(step2)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(step2[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))


def decode(key, string):
    """Function to decode secret client data using key.."""

    # TODO...

    return


def main():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Encode or decode a given string.',
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50))
    parser.add_argument('-e', '--encode', metavar='"string"',
                        help='Encode a given string')
    parser.add_argument('-d', '--decode', metavar='"string"',
                        help='Decode a given string')
    args = parser.parse_args()

    if args.encode is not None:
        print(encode(superstrongkey, args.encode))
    elif args.decode is not None:
        print(decode(superstrongkey, args.decode))
    else:
        print("\nMissing argument(s).\n\n")
        parser.print_help()
    return

if __name__ == '__main__':
    main()
