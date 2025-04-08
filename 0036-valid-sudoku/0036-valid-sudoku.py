class Solution(object):
    def isValidSudoku(self, board):
        # hotizontal
        for i in range(9):
            exists = [False]*10
            for j in range(9):
                if board[i][j] == ".": continue
                if exists[int(board[i][j])] == False: exists[int(board[i][j])]=True
                else: return False
        
        #vertical
        for j in range(9):
            exists = [False]*10
            for i in range(9):
                if board[i][j] == ".": continue
                if exists[int(board[i][j])] == False: exists[int(board[i][j])]=True
                else: return False
        
        #in the square
        for x in range(3):
            for y in range(3):
                exists = [False]*10
                for i in range(3):
                    for j in range(3):
                        if board[i+3*x][j+3*y] == ".": continue
                        elif exists[int(board[i+3*x][j+3*y])] == False: exists[int(board[i+3*x][j+3*y])]=True
                        else: return False

        return True

