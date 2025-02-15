class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for index, n in enumerate(nums): 
            needed = target - nums[index]
            if needed in seen: 
                return [seen[needed], index]
            seen[n] = index

