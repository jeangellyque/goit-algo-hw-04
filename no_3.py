import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_tree(directory: Path, prefix: str = "") -> None:
    """Рекурсивно виводить вміст директорії у вигляді дерева."""
    try:
        entries = sorted(
            directory.iterdir(),
            key=lambda entry: (not entry.is_dir(), entry.name.lower()),
        )
    except OSError as error:
        print(f"{prefix}{Fore.RED}[Помилка читання: {error}]{Style.RESET_ALL}")
        return

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        branch = "└── " if is_last else "├── "
        entry_prefix = prefix + ("    " if is_last else "│   ")

        if entry.is_dir():
            print(f"{prefix}{branch}{Fore.BLUE}{entry.name}{Style.RESET_ALL}")
            print_tree(entry, entry_prefix)
        else:
            print(f"{prefix}{branch}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Використання: python {Path(sys.argv[0]).name} <шлях_до_директорії>")
        return 1

    directory = Path(sys.argv[1]).expanduser()
    if not directory.exists():
        print(f"Помилка: шлях не існує: {directory}", file=sys.stderr)
        return 1
    if not directory.is_dir():
        print(f"Помилка: шлях не веде до директорії: {directory}", file=sys.stderr)
        return 1

    init(autoreset=False)
    print(f"{Fore.BLUE}{directory.name or directory}{Style.RESET_ALL}")
    print_tree(directory)
    return 0


if __name__ == "__main__":
    sys.exit(main())
