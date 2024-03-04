class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(idx, path):
            if len(path) == k:
                res.append(path[:])

            for i in range(idx, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()
        res = []
        backtrack(1, [])
        return res