class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        a = 0
        b = 0
        c = 0

        for i in range(len(piles)):
            if len(piles) == 0:
                break
            else:
                a += piles[-1]
                piles.pop()

                b += piles[-1]
                piles.pop()
                
                c += piles[0]
                piles.pop(0)

        return b
