from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset_list = []
        for i in range(len(nums)+1):
            subset_list.extend(list(combinations(nums, i)))
        return subset_list
