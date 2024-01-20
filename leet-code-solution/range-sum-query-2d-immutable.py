class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n=len(matrix)
        m=len(matrix[0])
        self.grid=[[0]*(m+1) for _ in range(n+1)]
        #prefix = [[0 for _ in range(m + 1)] for __ in range(n + 1)] 

        for i in range(n):
            for j in range(m):
                self.grid[i+1][j+1]=matrix[i][j]+self.grid[i][j+1]+self.grid[i+1][j]-self.grid[i][j]
        print(self.grid)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.grid[row2+1][col2+1]-self.grid[row2+1][col1]-self.grid[row1][col2+1]+self.grid[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)