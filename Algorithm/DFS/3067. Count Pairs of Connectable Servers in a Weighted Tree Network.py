
from collections import defaultdict
class Solution:
    def countPairsOfConnectableServers(self, edges: list[list[int]], signalSpeed: int) -> list[int]:

        # a,b 通过c连接
        # a<b a!=c b!=c --- a != b != c and a < b
        # a~c的距离可以被 signalSpeed整除
        # b~c的距离可以被 signalSpeed整除
        # a～c 和 b~c 路线不共享
        
        # defaultdict: when key does,'t exist, create this key with default value 0
        # create graph
        graph = defaultdict(list)
        for a , b , d in edges:
            graph[a].append((b , d))
            graph[b].append((a , d))

        
        # deep first search
        def dfs(n : int) -> int :
            # caculate
            def helper(n:int , pre_n:int , cur_d:int)-> int :
                res = 0
                for new_n , d in graph[n]:
                    if new_n != pre_n:
                        res += helper(n = new_n, pre_n = n , cur_d = cur_d + d)
                if not (cur_d % signalSpeed):
                    res += 1
                return res
            
            n_pairs = 0
            n_nodes = []
            for new_n , d in graph[n]:
                n_nodes.append(helper(new_n, n, d))
                
            for n1 in range(len(n_nodes)):
                for n2 in range(n1+1, len(n_nodes)):
                    n_pairs += n_nodes[n1] * n_nodes[n2]
            return n_pairs
            
        result = []
        for nodeIndex in range(len(graph)):
            result.append(dfs(nodeIndex))
        
        print(result)
        return result
        

solution = Solution()
solution.countPairsOfConnectableServers([[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]] , 1)



        