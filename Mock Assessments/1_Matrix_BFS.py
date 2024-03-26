class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)  # rows
        n = len(mat[0]) # cols
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        dist = [[float('inf')] * n for _ in range(m)]
        queue = deque()
    
        # Enqueue all cells with 0 and set distance to 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    dist[i][j] = 0

        # BFS to update distances
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        return dist