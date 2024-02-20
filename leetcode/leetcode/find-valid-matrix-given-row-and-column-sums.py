class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
       matrix = [ [0 for _ in range (len(colSum))] for _ in range(len(rowSum))]
       for row in range(len(rowSum)):
           for col in range (len(colSum)):
               num = min(rowSum[row],colSum[col])
               matrix[row][col] = num
               rowSum[row] -= num
               colSum[col] -= num

       return matrix