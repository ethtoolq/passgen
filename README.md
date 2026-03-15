# Password Generator

Password Generator — a simple Python utility for generating passwords from letters and digits. It generates a specified number of passwords of a given length and saves them to a text file — one password per line. The module secrets is used for randomness.

## Usage
```
bash
python3 password_gen.py -n 10 -l 16 -o passwords.txt
```
## Parameters

    -n, --number — number of passwords (default 10)
    -l, --length — password length (default 16)
    -o, --out — output file name (default passwords_YYYYMMDD_HHMMSS.txt)

## Requirements

    Python 3.6+

Use a password manager to store generated passwords.

## License

MIT
