from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()
        path = []
        def backtrack(idx):
            if sum(path) == target:
                ans.add(tuple(path[:]))
                return
            
            elif sum(path) > target:
                return 
            x = 0
            for i in range(idx, len(candidates)):
                if candidates[i] != x:
                    path.append(candidates[i])
                    backtrack(i+1)
                    x = path.pop()
        #import itertools
        #res = list(ans for ans,_ in itertools.groupby(ans))
        backtrack(0)
        
        return ans
