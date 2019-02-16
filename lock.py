import argparse


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


def get_pages(interval: str) -> list:
    pages = []

    for page in interval.strip("[]").split(","):
        page = page.split("-")

        for n in range(int(page[0]), int(page[-1]) + 1):
            pages.append(n)

    if min(pages) < 4:
        raise argparse.ArgumentTypeError(
            "%s is out of range (4-16)." % str(min(pages)))
    elif max(pages) > 16:
        raise argparse.ArgumentTypeError(
            "%s is out of range (4-16)." % str(max(pages)))

    return pages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mifare ultralight lock bytes translator.",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    subparsers = parser.add_subparsers(
        dest="action", help="Choose an action you wish to perform.")

    lock_parser = subparsers.add_parser(
        "lock",
        help="Calculate and return hex value for locking desired pages.")
    lock_parser.add_argument(
        "-p",
        "--pages",
        help="Pages (4-16) denoting which pages you wish to lock.",
        metavar="[4-16]",
        default=[],
        type=get_pages)
    lock_parser.add_argument(
        "--block-lock-otp",
        help="Freeze lock config for OTP",
        action="store_true")
    lock_parser.add_argument(
        "--block-lock-pages4",
        help="Freeze lock config for Page[4-9].",
        action="store_true")
    lock_parser.add_argument(
        "--block-lock-pages10",
        help="Freeze lock config for Page[10-15].",
        action="store_true")
    lock_parser.add_argument(
        "--lock-otp", help="Locks OTP Page.", action="store_true")

    args = parser.parse_args()
    return args


def main(args=None) -> None:
    if args.action == "lock":
        lock_bytes = init_bytes()

        for page in args.pages:
            lock_bytes[page_to_index(page)] = 1

        if args.lock_otp:
            lock_bytes[4] = 1

        if args.block_lock_pages10:
            lock_bytes[5] = 1

        if args.block_lock_pages4:
            lock_bytes[6] = 1

        if args.block_lock_otp:
            lock_bytes[7] = 1

        print(bin2hex(list_to_str(lock_bytes)))


def run() -> None:
    main(parse_args())


if __name__ == "__main__":
    run()
