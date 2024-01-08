class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        holder = 0
        seeker = 0
        max_count = 0

        while seeker < len(nums):
            if nums[seeker] == 0:
                k -= 1
            while k < 0:
                if nums[holder] == 0:
                    k += 1
                holder += 1
            seeker += 1
            max_count = max(max_count, seeker - holder)
           
        return max_count