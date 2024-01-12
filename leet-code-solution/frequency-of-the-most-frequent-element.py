class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        mx = 1
        l = 0
        sm = 0

        for r in range(len(nums)):
            sm +=nums[r]
            while l < r and nums[r]*(r-l+1) > sm + k:
                sm -= nums[l]
                l += 1
            mx = max(mx, r-l+1)
            
        return mx

