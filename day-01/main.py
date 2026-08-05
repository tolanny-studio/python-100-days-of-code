"""
Entry point for the Band Name Generator application.
"""

from termcolor import cprint
from bandname import BandName
from validateinput import validate_input

CITY_NAME_PROMPT = "\nWhat is your city name ? "
PET_NAME_PROMPT = "\nWhat is your pet name ? "


def get_input():
    # Get and store the city name.
    # Get and store the pet name.
    return (validate_input(CITY_NAME_PROMPT), validate_input(PET_NAME_PROMPT))


def main():
    """
    Create a band name and display it in green.

    This function creates an instance of the BandName class,
    generates a band name using the user's input, and prints
    the result to the terminal.
    """

    #  Displays a welcome message
    print("\nWelcome to the band name generator.")

    city_name, pet_name = get_input()

    # Create a BandName object
    band_name = BandName(city_name, pet_name)

    # Display the generated band name in green
    cprint(band_name, "green")


if __name__ == "__main__":
    # Run the program only when this file is executed directly
    main()
