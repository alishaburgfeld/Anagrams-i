import unittest
from character_match import is_character_match


class TestIsCharacterMatch(unittest.TestCase):
    def test_is_character_match(self):
        self.assertTrue(is_character_match("charm", "march"))
        self.assertFalse(is_character_match("zach", "attack"))
        self.assertTrue(is_character_match("CharM", "mARcH"))
        self.assertTrue(is_character_match("abcde2", "c2abed"))
        self.assertTrue(is_character_match("Anna Madrigal", "A man and a gril"))


if __name__ == "__main__":
    unittest.main()
