from __future__ import annotations

from typing import Dict, List, Tuple


WELCOME_MESSAGE = "Welcome to the assistant bot!"
GOODBYE_MESSAGE = "Good bye!"
HELLO_MESSAGE = "How can I help you?"
INVALID_COMMAND_MESSAGE = "Invalid command."
CONTACT_NOT_FOUND_MESSAGE = "Contact not found."
NO_CONTACTS_MESSAGE = "No contacts saved."


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command, *args = parts
    return command.lower(), args


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return INVALID_COMMAND_MESSAGE

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        return INVALID_COMMAND_MESSAGE

    name, phone = args
    if name not in contacts:
        return CONTACT_NOT_FOUND_MESSAGE

    contacts[name] = phone
    return "Contact updated."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 1:
        return INVALID_COMMAND_MESSAGE

    name = args[0]
    return contacts.get(name, CONTACT_NOT_FOUND_MESSAGE)


def show_all(contacts: Dict[str, str]) -> str:
    if not contacts:
        return NO_CONTACTS_MESSAGE

    return "\n".join(
        f"{name}: {phone}" for name, phone in sorted(contacts.items())
    )


def handle_command(command: str, args: List[str], contacts: Dict[str, str]) -> str:
    if command == "hello" and not args:
        return HELLO_MESSAGE
    if command == "add":
        return add_contact(args, contacts)
    if command == "change":
        return change_contact(args, contacts)
    if command == "phone":
        return show_phone(args, contacts)
    if command == "all" and not args:
        return show_all(contacts)
    if command in {"close", "exit"} and not args:
        return GOODBYE_MESSAGE
    return INVALID_COMMAND_MESSAGE


def main() -> None:
    contacts: Dict[str, str] = {}
    print(WELCOME_MESSAGE)

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        response = handle_command(command, args, contacts)
        print(response)

        if command in {"close", "exit"} and response == GOODBYE_MESSAGE:
            break


if __name__ == "__main__":
    main()
