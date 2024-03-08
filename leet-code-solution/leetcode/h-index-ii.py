class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = -1, len(citations)+1

        while left + 1 < right:
            mid = (left+right)//2
            key = bisect_left(citations , mid)
            if mid  <= len(citations) - key:
                left = mid
            else:
                right = mid

        return left