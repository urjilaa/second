class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def kthBit(n, k):
            if n == 1:
                return 0

            mid = 2**(n-1) 
            if k == mid:
                return 1
            elif k < mid:
                return kthBit(n-1, k)
            else:
                return kthBit(n-1, 2**n-k)^1
                
        return str(kthBit(n,k))