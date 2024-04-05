class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9

        def isSudoku(row , col , ch):
            row, col = int(row), int(col)
            for i in range(9):
                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False
                _i = 3*(row//3) + i//3
                _j = 3*(col//3) + i%3
                if board[_i][_j] == ch:
                    return False
            return True

        def fillSudoku(i , j):
            if i == n:
                return True
            if j == n:
                return fillSudoku(i+1 , 0)

            if board[i][j] == '.':
                for x in range(1,10):
                    if isSudoku(i , j , str(x)):
                        board[i][j] = str(x)

                        if fillSudoku(i , j+1):
                            return True
                        else:
                            board[i][j] = '.'
                return False
            else:
                return fillSudoku(i , j+1)
                
        fillSudoku(0 , 0)
                    
                        
        