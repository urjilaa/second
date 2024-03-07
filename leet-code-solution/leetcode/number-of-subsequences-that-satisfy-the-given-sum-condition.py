class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        def bisect(d, left, right):
            while left + 1 < right:
                mid = (left+right)//2
                if nums[mid] <= d:
                    left = mid
                else:
                    right = mid
            return left
        
        ans = 0
        for l in range(len(nums)):
            diff = target - nums[l]
            r = bisect(diff, l, len(nums))
            if (r-l) > 0:
                ans += 2**(r-l)
            elif nums[l]*2 <= target:
                ans += 1

        return ans%(10**9 + 7)