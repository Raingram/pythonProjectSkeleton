# Named __main__.py to mark this file as the entry-point.
# Allows for running like: `python3 -m hello_world <args>`
import argparse


def construct_greeting(name: str):
    """Inserts the user's name provided into the greeting message.

    :param name: Name of user to welcome.
    :return: Greeting string.
    """
    return f"Hello, {name}!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Hello World Example.")
    parser.add_argument("name", default="World", help="Name of user to welcome.")

    args = parser.parse_args()

    print(construct_greeting(args.name))

