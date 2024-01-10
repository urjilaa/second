class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = [x for x, _ in points]
        points.sort()

        max_diff = 0
        for i in range(1, len(points)):
            max_diff = max(max_diff, points[i] - points[i-1])
        
        return max_diff