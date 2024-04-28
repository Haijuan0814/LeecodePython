from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        count = [1] * n
        res = [0] * n
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs1(node , parent):
            for child in graph[node]:
                if child != parent:
                    dfs1(child ,  node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]
        
        def dfs2(node , parent):
            for child in graph[node]:
                if child != parent:
                    # ???
                    # res[child] = res[node] + (n - count[child]) - count[child]
                    res[child] = res[node] - count[child] + (n - count[child])
                    dfs2(child, node)
                    

        
        dfs1(0 , -1)
        dfs2(0 , -1)

        return res
                


            


        


        