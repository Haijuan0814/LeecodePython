class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        for x , y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
       
        def dfs(vis , sour , desc , gra):
            if sour == desc:
                return True

            vis[sour] = True
            for neighbor in gra[sour]:
                if not vis[neighbor]:
                    if dfs(vis , neighbor , desc , gra):
                        return True
            return False

        
        visited = [False] * n
        res = 0
        res = dfs(visited , source , destination , graph)
        return res
        