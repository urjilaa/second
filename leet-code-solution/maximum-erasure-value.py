class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        score = 0
        max_score = score
        l = 0
        
        for r in range(len(nums)):
            score += nums[r]
            d[nums[r]] += 1
            while d[nums[r]] > 1:
                d[nums[l]] -= 1
                score -= nums[l]
                l += 1
            max_score = max(max_score, score)
        return max_score
