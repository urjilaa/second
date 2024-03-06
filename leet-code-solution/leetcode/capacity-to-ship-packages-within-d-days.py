class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        right = sum(weights)
        left = max(weights)

        while left <= right:
            mid = (left+right)//2
            count = 0
            summ = 0
            for i in weights:
                summ += i
                if summ == mid:
                    summ = 0
                    count += 1
                elif summ > mid:
                    count += 1
                    summ = i
            if summ != 0:
                count += 1

            if count <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left