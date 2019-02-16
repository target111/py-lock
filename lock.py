def init_bytes() -> list:
    bytes = []

    for _ in range(16):
        bytes.append(0)

    return bytes


def page_to_index(page: int) -> int:
    if page >= 4 and page <= 7:
        return (7 - page)

    return (23 - page)


def list_to_str(l: list) -> str:
    return "".join([str(item) for item in l])


def bin2hex(binary: str) -> hex:
    return f'{int(binary, 2):0{(len(binary)+3)//4}x}'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mifare ultralight lock bytes translator.",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    subparsers = parser.add_subparsers(
        dest="action", help="Choose an action you wish to perform.")

    lock_parser = subparsers.add_parser(
        "lock",
        help="Calculate and return hex value for locking desired pages.")
    lock_parser.add_argument()