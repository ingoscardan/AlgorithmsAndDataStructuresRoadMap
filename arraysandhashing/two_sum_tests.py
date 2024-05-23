import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_two_sums_case_target_nine(self):
        nums = [2, 7, 11, 15]
        target = 9

        self.assertEqual([0, 1], two_sum(nums, target))
