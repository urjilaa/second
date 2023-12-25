class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0

        for i in range(n):  
            res += mat[i][i] # the left side diagonal
            res += mat[i][n-1-i] # the right side diagonal or reverse of left side

         # if the diagonal matrix cross and use one element twice minus that element which happens if len(mat) is even 
        if n % 2 != 0:
            res -= mat[n//2][n//2]

        return res