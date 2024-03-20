from collections import defaultdict
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:

        def dfs(index : int, preIndex = -1 , minScore = 0) -> int :

            if index and graph[index] == [preIndex]:
                return values[index]

            for nextIndex in graph[index]:
                if nextIndex != preIndex:
                    minScore += dfs(nextIndex , index)

            return min(minScore , values[index])


        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b) 
            graph[b].append(a) 

        return sum(values) - dfs(0)

        

        