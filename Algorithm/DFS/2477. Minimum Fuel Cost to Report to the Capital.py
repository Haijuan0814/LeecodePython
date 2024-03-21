class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        def dfs(i , prev , people = 1):
            for x in graph[i]:
                if x == prev:
                    continue
                people += dfs(x , i)
            if i:
                self.ans +=  (int(ceil(people / seats)))
            else:
                self.ans += 0
            return people
        
        graph = defaultdict(list)
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        self.ans = 0
        dfs(0 , 0)
        return self.ans
                