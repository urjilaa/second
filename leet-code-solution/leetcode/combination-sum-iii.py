class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        path = []
        def backtrack(start):
            if sum(path) == n and len(path) == k:
                res.add(tuple(path[:]))
            
            x = 0    
            for i in range(start+1, 10):
                if i != x:
                    path.append(i)
                    backtrack(i)
                    x = path.pop()
        backtrack(0)
        return res

