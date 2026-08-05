"""
Band Name Generator.

This module defines the BandName class, which prompts the user for
their city and pet names, then generates a simple band name.
"""

from termcolor import cprint


class BandName:
    """
    Generate a band name from the user's city and pet names.

    The class collects validated user input and formats it into
    a band name that can be printed directly.
    """

    def __init__(self):
        """
        Initialize a BandName object.

        Initializes the city and
        pet name attributes.
        """
        print("\nWelcome to the band name generator.")
        self.city_name = ""
        self.pet_name = ""

    def validate_input(self, prompt):
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
            _prompt = input(prompt)

            # Ensure the input has at least three characters.
            if len(_prompt) < 3:
                cprint(
                    "\nInvalid input ⛔ Input should be more than 2 characters",
                    "red",
                )
                continue

            return _prompt

    def create_band(self):
        """
        Collect the city and pet names from the user.

        The collected values are stored in the object's attributes
        for later use when generating the band name.
        """
        # Get and store the city name.
        self.city_name = self.validate_input("\nWhat is your city name ? ")

        # Get and store the pet name.
        self.pet_name = self.validate_input("\nWhat is your pet name ? ")

    def __str__(self):
        """
        Return the formatted band name.

        Returns:
            str: A string containing the generated band name.
        """
        return (
            f"\nThe name of your band is {self.city_name.title()} {self.pet_name}"
        )