class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tot_sum = sum(nums)
        prefix = 0
        res = [0]*n

        for i in range(n):
            tot_sum -= nums[i]

            left = nums[i] * i - prefix
            right = tot_sum - nums[i] * (n-i-1)

            prefix += nums[i]
            res[i] = left + right
        
        return res