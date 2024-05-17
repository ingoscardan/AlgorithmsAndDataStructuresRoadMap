def contains_duplicates_naive(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    """
    occurrences_dictionary = {}

    for num in nums:
        if num not in occurrences_dictionary:
            occurrences_dictionary[num] = 0
        occurrences_dictionary[num] += 1

    for value in occurrences_dictionary.values():
        if value > 1:
            return True

    return False


def contains_duplicates_with_sets(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    """
    occurrences_dictionary = {}

    for num in nums:
        if num not in occurrences_dictionary:
            occurrences_dictionary[num] = 0
        occurrences_dictionary[num] += 1

    unique_occurrences = set(occurrences_dictionary.values())
    n = len(unique_occurrences)
    if n == 1 and 1 in unique_occurrences:
        return False

    return True


def contains_duplicates_sorting_list_of_nums(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    """

    # Sort the list of nums
    nums.sort()

    left_ptr = 0

    # [1,2,3,1] sort -> [1, 1, 2, 3]
    for right_ptr in range(len(nums)):
        value = nums[left_ptr]
        if nums[right_ptr] == value and right_ptr - left_ptr + 1 > 1:
            return True
    return False


def contains_duplicates_only_sets(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    """
    uniques = set()
    for num in nums:
        if num in set:
            return True
        else:
            uniques.add(num)
    return False
