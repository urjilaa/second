class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       result = sum(range(0, len(nums)+1)) - sum(nums)
       return result

