class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        score = 0
        max_score = 0
        l = 0

        for r in range(len(nums)):
            if d[nums[r]] == 0:
                score += nums[r]
                d[nums[r]] += 1
            else:
                while l < r and nums[l] != nums[r]:
                    d[nums[l]] -= 1
                    score -= nums[l]
                    l += 1
                l += 1
            max_score = max(max_score, score)
        return max_score

