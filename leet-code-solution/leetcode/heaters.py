class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for i in houses:
            left = heaters[bisect_left(heaters, i) - 1] if bisect_left(heaters, i) > 0 else float('-inf')
            right = heaters[bisect_left(heaters, i)] if bisect_left(heaters, i) < len(heaters) else float('inf')
            ans = max(ans, min(i - left, right - i))
            
        return ans