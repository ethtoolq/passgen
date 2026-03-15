import argparse
import secrets
import string
from datetime import datetime


# random passgen
def gen_password(length: int) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Random Password Generator")

    parser.add_argument("-n", "--number", type=int, default=10,
                        help="Number of passwords")
    parser.add_argument("-l", "--length", type=int, default=16,
                        help="Password length")
    parser.add_argument("-o", "--out",
                        default=f"passwords_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        help="File to save")

    args = parser.parse_args()

    # parameter check
    if args.number < 1 or args.length < 1:
        print("Параметры должны быть >= 1")
        return

    # generate and record passwords
    with open(args.out, "w", encoding="utf-8") as f:
        for _ in range(args.number):
            f.write(gen_password(args.length) + "\n")

    print(f"Generated {args.number} password. File: {args.out}")


if __name__ == "__main__":
    main()
