import unittest
from valid_anagram import is_anagram_sorting


class TestValidAnagrams(unittest.TestCase):
    def test_is_anagram_sorting_true_when_both_have_same_length(self):
        s = "anagram"
        t = "nagaram"
        self.assertEqual(True, is_anagram_sorting(s, t))  # add assertion here

    def test_is_anagram_sorting_false_when_both_have_different_length(self):
        s = "anagram"
        t = "nagaam"
        self.assertEqual(False, is_anagram_sorting(s, t))  # add assertion here


if __name__ == '__main__':
    unittest.main()
