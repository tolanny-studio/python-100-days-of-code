from termcolor import cprint

MINIMUM_CHARACTER = 3


def validate_input(prompt):
    """
    Prompt the user for input until a valid response is entered.

    A valid input must contain at least three characters.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        str: The validated user input.
    """
    while True:
        # Read input from the user.
        _prompt = input(prompt).strip()

        # Ensure the input has at least three characters.
        if len(_prompt) < MINIMUM_CHARACTER:
            cprint(
                "\nInvalid input ⛔ Input should be more than 2 characters",
                "red",
            )
            continue

        return _prompt
