class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        dp = {}

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[(i,j)] = (0 , 0)
                else:
                    x = dp[(i,j-1)][0]+1 if j > 0  else 1
                    y = dp[(i-1,j)][1]+1 if i > 0  else 1
                    dp[(i,j)] = (x , y)
                    ans = max(x, y , ans)
                    minWidth = x
                    for r in range(i-1,i-y,-1):
                        minWidth =  min(minWidth , dp[(r,j)][0])
                        hieght = i - r + 1
                        ans = max(ans , minWidth * hieght)
        return ans
        