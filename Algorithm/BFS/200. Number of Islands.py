class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        read = [[False for x in range(m)] for y in range(n)]
        def dfs(i,j):
            if i < 0 or i >= m  or j < 0 or j >= n:
                return
            if grid[i][j] == '1':
                grid[i][j] = '2'
                dfs(i,j-1)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i+1,j)
        num = 0
        for i, row in enumerate(grid):
            for j,val in enumerate(row):
                if val == '1':
                    num += 1
                    dfs(i,j)
        return num
            
            
        