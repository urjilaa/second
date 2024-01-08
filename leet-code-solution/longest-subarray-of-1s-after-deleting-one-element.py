class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        holder = 0
        seeker = 0
        changed = 0
        max_count = 0

        while seeker < len(nums):
            if nums[seeker] == 0:
                changed += 1
            while changed > 1:
                if nums[holder] == 0:
                    changed -= 1
                holder += 1
            seeker += 1
            max_count = max(max_count, seeker - holder -1)
        
        return max_count