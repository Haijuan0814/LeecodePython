class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])

        def dfs(x , y , group):
            if x < 0 or x >= m or y < 0 or y >= n or land[x][y] != 1:
                return []

            land[x][y] = 2
            group[0] = min(group[0],x)
            group[1] = min(group[1],y)
            group[2] = max(group[2],x)
            group[3] = max(group[3],y)
           

            dfs(x,y-1,group)
            dfs(x,y+1,group)
            dfs(x-1,y,group)
            dfs(x+1,y,group)

        result = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    group = [i , j , i , j]
                    dfs(i, j , group)
                    result.append(group)
                #result.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])

        return result

        