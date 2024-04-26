class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid) 

        dp = [ [-1] * n for _ in range(n)]

        for i in range(n):
            dp[0][i] = grid[0][i]
        
        for i in range(1,n):
            for j in range(n):
                tmp = float('inf')
                for k in range(n):
                    if j != k:
                        tmp = min(tmp ,  grid[i][j] + dp[i-1][k])
                dp[i][j] = tmp

        print(dp)
        return min(dp[n-1])

        