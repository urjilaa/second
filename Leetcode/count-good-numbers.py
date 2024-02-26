class Solution:
    store = {}
    def countGoodNumbers(self, n: int) -> int:
        if n == 2:
            return 20
        elif n == 1:
            return 5
        if n not in self.store:
            if n%2 == 0:
                self.store[n] = (self.countGoodNumbers(n-1) * 4)%(10**9 + 7)
            else:
                self.store[n] = (self.countGoodNumbers(n//2) * self.countGoodNumbers((n//2)+1))%(10**9 + 7)
            return (self.store[n])%(10**9 + 7)
        else:
            return (self.store[n])%(10**9 + 7)