class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sum(n):
            s = 0
            for i in nums:
                s += ceil(i/n)
            return s

        left, right = 0, max(nums)
        while left + 1 < right:
            mid = (left+right)//2
            if sum(mid) > threshold:
                left = mid
            else:
                right = mid
        return right 