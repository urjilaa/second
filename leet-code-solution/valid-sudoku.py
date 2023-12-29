class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for row in range(len(board)):
            s= set()
            for col in range(len(board[0])):
                if board[row][col] != '.' and board[row][col] in s:
                    return False
                else:
                    s.add(board[row][col])
     

        s = set()
        for col in range(len(board[0])):
            s = set()
            for row in range(len(board)):
                if board[row][col] != '.' and board[row][col] in s:
                    return False
                else:
                    s.add(board[row][col])
       
        s = set()
        for k in range(0, 9, 3):
            s = set()
            for i in range(k, k+3):
                for j in range(0, 3):
                    if board[i][j] != '.' and board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
            
            s = set()
            for i in range(k, k+3):
                for j in range(3, 6):
                    if board[i][j] != '.' and board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
            
            s = set()
            for i in range(k, k+3):
                for j in range(6, 9):
                    if board[i][j] != '.' and board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j]) 
        print(s)
        return True
    
