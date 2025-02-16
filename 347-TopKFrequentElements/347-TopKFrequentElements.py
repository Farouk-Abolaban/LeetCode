class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]
        result = []

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        for i, cnt in count.items(): 
            bucket[cnt].append(i)

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k: 
                    return result