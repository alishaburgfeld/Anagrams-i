# Don't forget to run your tests!

from collections import Counter
from string import ascii_letters, digits


def is_character_match(string1, string2):
    """
    This function returns True if the two strings are anagrams of each other regardless of case.

    Args:
		string1 (str): The first string to compare.
		string2 (str): The second string to compare.

    Returns:
		bool: True if the two strings are anagrams of each other regardless of case.
    """

    valid_chars = set(ascii_letters) | set(digits)
	
    string1_counts = Counter(c.lower() for c in string1 if c in valid_chars)
    string2_counts = Counter(c.lower() for c in string2 if c in valid_chars)

    return string1_counts == string2_counts
