class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        holder = 0
        min_len = float('inf')
        sum = 0

        for seeker in range(len(nums)):
            sum += nums[seeker]
            while sum >= target:
                min_len = min(min_len, seeker - holder + 1)
                sum -= nums[holder]
                holder += 1
         
        return 0 if min_len == float('inf') else min_len