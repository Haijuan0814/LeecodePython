class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # Greedy Algorithm
        # used for (1) 
        if len(points) < 2:
            return len(points)

        points = sorted(points , key = lambda x : x[1])
        firstPoint = points[0]
        count = 1
        for i in range(1, len(points)):
            if firstPoint[1]>=points[i][0] and firstPoint[1]<=points[i][1]:
                continue
            else:
                firstPoint = points[i]
                count += 1
        return count
    
    """  贪心算法
    1、找零钱问题： 
    给定一定面额的硬币，以及一个需要找零的金额，要求找零的硬币数量最少。贪心策略是每次尽量使用面额最大的硬币。

    2、活动选择问题： 
    给定一组活动，每个活动都有开始时间和结束时间，要求选择最大数量的互不冲突的活动。贪心策略是选择结束时间最早的活动。

    3、背包问题的部分解决方案： 
    在背包问题中，有时候贪心算法可以用来找到一个部分解决方案，但不能保证一定得到最优解。例如，分数背包问题中，可以优先选择单位价值最高的物品放入背包。

    4、最小生成树问题： 
    在图论中，最小生成树问题是指在一个连通加权无向图中找到一个边的子集，这些边构成了一棵树，使得这棵树中所有边的权值之和最小。Kruskal 和 Prim 算法都是贪心算法的经典应用。
    """



