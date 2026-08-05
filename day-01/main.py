"""
Entry point for the Band Name Generator application.
"""

from termcolor import cprint
from bandname import BandName


def main():
    """
    Create a band name and display it in green.

    This function creates an instance of the BandName class,
    generates a band name using the user's input, and prints
    the result to the terminal.
    """
    
    #  Displays a welcome message     
    print("\nWelcome to the band name generator.")
    
    # Create a BandName object
    band_name = BandName()

    # Generate the band name
    band_name.create_band()

    # Display the generated band name in green
    cprint(band_name, "green")


if __name__ == "__main__":
    # Run the program only when this file is executed directly
    main()
