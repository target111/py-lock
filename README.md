# Py-lock
Py-lock is a simple python tool designed to simplify the process of mifare ultralight lock-bytes manipulation.

## Usage ##
```
./lock.py
usage: lock.py [-h] {lock,info} ...

Mifare ultralight lock bytes translator.

positional arguments:
  {lock,info}  Choose the action you wish to perform.
    lock       Calculate and return hex value for locking desired pages.
    info       Translate lock bytes from hex to human readable output.

optional arguments:
  -h, --help   show this help message and exit
```
