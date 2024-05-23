def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
    target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    :param nums:
    :param target:
    :return:
    """
    numbers_map = {}

    for i in range(len(nums)):
        difference = target - nums[i]

        if difference in numbers_map:
            return [numbers_map[difference], i]
        else:
            numbers_map[nums[i]] = i
