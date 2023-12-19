class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num = list(range(1, n+1))
        idx = k - 1

        while n > 1:
            idx %= n
            num.remove(num[idx])
            idx += k-1
            n -= 1
        return num[0]

