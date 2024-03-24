class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        if not grid or len(grid) < 2:
            return False

        m = len(grid)
        n = len(grid[0])
        check = [[0] * n for _ in range(m)]

        def dfs(curr , curr_val):
            visited = set()
            queue = [curr]
            while len(queue) > 0:
                cell = queue.pop()
                if cell in visited:
                    return True if len(visited) >= 4 else False
                visited.add(cell)
                i, j = cell[0], cell[1]
                check[i][j] = 1
                if i > 0 and check[i-1][j] == 0 and grid[i-1][j] == curr_val:
                    queue.append((i-1,j))
                if i < m-1 and check[i+1][j] == 0 and grid[i+1][j] == curr_val:
                    queue.append((i+1,j))
                if j > 0 and check[i][j-1] == 0 and grid[i][j-1] == curr_val:
                    queue.append((i,j-1))
                if j < n-1 and check[i][j+1] == 0 and grid[i][j+1] == curr_val:
                    queue.append((i,j+1))
            return False
        
        for i in range(m):
            for j in range(n):
                if check[i][j] == 0:
                    if dfs((i,j) , grid[i][j]):
                        return True
        return False

        
        
        
        
        