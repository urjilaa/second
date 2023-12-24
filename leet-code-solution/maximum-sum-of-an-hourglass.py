class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        value = 0
        highest = 0
        
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                value = sum(grid[row][col:col+3]) + grid[row+1][col+1] + sum(grid[row+2][col:col+3])
                highest = max(highest, value)
                
        return highest