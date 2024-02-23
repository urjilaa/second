class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mx = 0
        i = 0
        s = 0
        while i < len(nums):
            s += nums[i]
            mx = max(mx, ceil(s/(i+1)))
            print(i, s, mx) 
            i += 1
            
        return mx
            