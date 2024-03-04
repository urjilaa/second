class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(idx, path):
            if sum(path) == target:
                ans.append(path[:])
                return
            
            elif sum(path) > target:
                    return 
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path)
                path.pop()
        backtrack(0,[])
        return ans