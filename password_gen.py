import argparse
import secrets
import string
from datetime import datetime

def gen_password(length: int) -> str:
    alphabet = string.ascii_letters + string.digits  # без специальных знаков
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Random Password Generator (letters + digits)")
    parser.add_argument("-n", "--number", type=int, default=10, help="Количество паролей (по умолчанию 10)")
    parser.add_argument("-l", "--length", type=int, default=16, help="Длина пароля (по умолчанию 16)")
    parser.add_argument("-o", "--out", default=f"passwords_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        help="Файл вывода (по умолчанию passwords_YYYYMMDD_HHMMSS.txt)")
    args = parser.parse_args()

    if args.number < 1 or args.length < 1:
        print("Параметры --number и --length должны быть >= 1")
        return

    with open(args.out, "w", encoding="utf-8") as f:
        for _ in range(args.number):
            f.write(gen_password(args.length) + "\n")

    print(f"Сгенерировано {args.number} паролей длиной {args.length}. Сохранено в {args.out}")

if __name__ == "__main__":
    main()
