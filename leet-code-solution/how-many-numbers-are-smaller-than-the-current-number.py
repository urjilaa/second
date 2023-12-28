class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for l in range(len(nums)):
            count = 0
            for r in range(len(nums)):
                if nums[l] > nums[r]:
                    count += 1
            res.append(count)

        return res

