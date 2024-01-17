class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l = 0
        for l in range(len(nums)):
            l_sum = sum(nums[:l])
            r_sum = sum(nums[l+1:])
            if l_sum == r_sum:
                return l
        
        return -1