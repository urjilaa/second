class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        point= sorted(points, key = lambda x:sqrt(x[0]**2 + x[1]**2))[:k]
        return point
