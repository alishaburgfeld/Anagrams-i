# Don't forget to run your tests!




from collections import Counter


def is_character_match(string1, string2):
    """
    This function returns True if the two strings are anagrams of each other regardless of case.

    Args:
        string1 (str): The first string to compare.
        string2 (str): The second string to compare.

    Returns:
        bool: True if the two strings are anagrams of each other regardless of case.
    """


    # result = 0
    # for c in string:
    #     if c == target:
    #         result += 1

    # return result

    # for c in string1 + string2:
    #     if string1.count(c) != string2.count(c):
    #         return False

    # return True

    return Counter(string1) == Counter(string2)

    return "".join(sorted(string1.lower())).strip() == "".join(sorted(string2.lower())).strip()
