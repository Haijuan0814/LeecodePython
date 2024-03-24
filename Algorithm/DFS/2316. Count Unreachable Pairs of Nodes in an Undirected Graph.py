class Solution:
    count = 0
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        # initial a graph
        graph = defaultdict(list)
        for x , y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # caculate the visited node until i-th row
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            return

        
        preVisited = 0 
        res = 0
        total = n
        for i in range(n):   
            if i not in visited:
                dfs(i)
                # for node i: the no. that can be visited, can imagine as the i-th row
                tmp = len(visited) - preVisited  
                total -= tmp
                res += (tmp * total)
                preVisited = len(visited)

        return res