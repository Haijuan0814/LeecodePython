
# "backtrack"通常指的是在解决问题时使用的一种算法技巧，通常用于回溯搜索和深度优先搜索。
# 回溯算法尝试在解空间中搜索所有可能的解，当遇到无法满足条件的情况时，就会回溯到上一个状态，然后尝试其他可能的路径。
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # i,j --> index of the board
        # k --> the length of correspond chars

        # c a a
        # a a a
        # b c d
        def backtrack (i , j , k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board):
                return False
            if j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[k]:
                return False
                
            char = board[i][j]
            board[i][j] = '' 
            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True
            board[i][j] = char

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if backtrack(i , j , 0):
                    return True
        return False

