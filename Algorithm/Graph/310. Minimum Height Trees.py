class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 or not edges:
            return [0]

        graph = defaultdict(set)
        depth   = [0] * n
        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        leaves = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            nextLeaves = []
            for leaf in leaves:
                # 从leaf节点的相邻节点集合中获取第一个节点，并将其赋值给变量u。
                u = next(iter(graph[leaf]))
                graph[u].remove(leaf)
                if len(graph[u]) == 1:
                    nextLeaves.append(u)
            leaves = nextLeaves
        return leaves
