class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0

        for l in range(len(nums)):
            for r in range(len(nums)):
                if nums[l] + nums[r] < target and l != r:
                    count += 1
                
        return count//2
