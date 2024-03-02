class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_mx = []
        col_mx = []
        for i in grid:
            row_mx.append(max(i))
        #print(row_mx)  
        
        for i in range(len(grid[0])):
            temp_mx = 0
            for j in range(len(grid)):  
                if grid[j][i] > temp_mx:
                    temp_mx = grid[j][i]
            col_mx.append(temp_mx)
        #print(col_mx)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(row_mx[i], col_mx[j]) - grid[i][j]
                #print(res, grid[i][j], row_mx[i], col_mx[j])
        #print(res, "---------------------------------")
        return res