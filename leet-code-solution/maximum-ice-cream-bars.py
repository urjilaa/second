class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        count = 0
        costs.sort()

        for i in range(len(costs)):
            if res + costs[i] <= coins and costs[i] < coins:
                res += costs[i]
                count += 1

        return count