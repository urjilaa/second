class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wd = [i for i in word]
        #print(wd)
        path = [] 
        pos = set()
        up = False
        down = False
        row = False
        col = False
        
        def backtrack(i, j):
            nonlocal up,down,row,col
            if (up or down or row or col):
                return True

            if path != wd and len(path) >= len(wd):
                return
            
            if path and path[-1] != wd[len(path)-1]:
                return 

            if (i, j) not in pos and i < len(board) and j < len(board[0]):
                path.append(board[i][j])
                pos.add((i, j))

                if path == wd:
                    return True

                if i > 0 and (i-1, j) not in pos:
                    up = backtrack(i-1, j)
                if j > 0 and (i, j-1) not in pos:
                    down = backtrack(i, j-1)

                if j < len(board[0]) and (i, j+1) not in pos:
                    col = backtrack(i, j+1)
                if i < len(board) and (i+1, j) not in pos:
                    row = backtrack(i+1, j)
                
                #print(path)
                path.pop()
                pos.remove((i, j))

            return (up or down or row or col)

        for i in range(len(board)): #row
            for j in range(len(board[0])): #col
                if backtrack(i, j):
                    return True

        return False
