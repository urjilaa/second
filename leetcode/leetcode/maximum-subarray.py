class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        curr = nums[0]

        for i in nums[1:]:
            curr = max(i, curr+i)
            mx = max(mx, curr)
            
        return mx    