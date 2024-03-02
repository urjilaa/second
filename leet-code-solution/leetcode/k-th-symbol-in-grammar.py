class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def grammer(n, k , left, right):
            if n == 1:
                return 0
            half = (left + right)/2
            if k <= half:
                return grammer(n-1, k , left, half)
            else:
                prev = grammer(n-1, k, half, right)
                if prev == 0:
                    return 1
                else:
                    return 0

        return grammer(n, k , 0 , 2**(n-1))