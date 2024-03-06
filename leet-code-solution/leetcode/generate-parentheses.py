class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(op_cnt, cl_cnt):
            if len(path) == 2*n:
                res.append(''.join(path))
            if op_cnt < n:
                path.append('(')
                backtrack(op_cnt + 1, cl_cnt)
                path.pop()
            if cl_cnt < op_cnt:
                path.append(')')
                backtrack(op_cnt, cl_cnt + 1)
                path.pop()
        backtrack(0, 0)
        
        return res