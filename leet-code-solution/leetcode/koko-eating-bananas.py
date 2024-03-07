class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 0, max(piles)
        while left + 1 < right:
            mid = (left+right)//2
            s = 0
            for i in piles:
                s += ceil(i/mid)

            if s > h:
                left = mid
            else:
                right = mid
                
        return right
                    
                
