class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0

        for i in range(len(points)-1):
            for j in range(len(points[i])):
                x = abs(points[i][0] - points[i+1][0])
                y = abs(points[i][1] - points[i+1][1])

            count += max(x, y)
            
        return count

