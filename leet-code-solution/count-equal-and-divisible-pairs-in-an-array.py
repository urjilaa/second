class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        
        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                if nums[l] == nums[r] and (l * r) % k == 0:
                    count += 1
               
        return count