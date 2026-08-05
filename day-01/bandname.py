"""
Band Name Generator.

This module defines the BandName class, which prompts the user for
their city and pet names, then generates a simple band name.
"""

class BandName:
    """
    Stores the city and pet names and formats them as a band name.
    """

    def __init__(self, city_name, pet_name):
        """
        Initialize a BandName object.

        Initializes the city and
        pet name attributes.
        """
        self._city_name = city_name
        self._pet_name = pet_name

    def __str__(self):
        """
        Return the formatted band name.

        Returns:
            str: A string containing the generated band name.
        """
        return f"\nThe name of your band is {self._city_name.title()} {self._pet_name}"
