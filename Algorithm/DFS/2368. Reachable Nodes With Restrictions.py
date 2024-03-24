class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        # solution 1: DFS

        block = [False] * n
        for n in restricted:
            block[n] = True
        graph = defaultdict(list)
        for x,y in edges:
            if not block[x] or not block[y]:
                graph[x].append(y)
                graph[y].append(x)

        self.count = 0
        def dfs(node:int):
            if block[node]:
                return
            block[node] = True
            self.count += 1
            neighbours = graph[node]
            for neighbour in neighbours:
                dfs(neighbour)
        dfs(0)
        return self.count

        # solution -2
        """ graph = defaultdict(list)
        block = set()
        for n in restricted:
            block.add(n)

        for x,y in edges:
            #if x not in restricted and y not in restricted:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        queue = deque([0])
        count = 1
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            for new in graph[cur]:
                if new in visited or new in block:
                    continue     
                queue.append(new)
                count += 1

        return count """

