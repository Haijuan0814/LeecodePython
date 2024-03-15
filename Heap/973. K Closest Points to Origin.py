class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        if len(points) <= k:
            return points

        # solution-1
        # return sorted(points, key=lambda i: dist(i, [0, 0]))[:k]

        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            total = pow(x,2) + pow(y,2)
            heapq.heappush(heap,[-total,[x,y]])

            if len(heap) > k:
                s,_ = heapq.heappop(heap)
        return [y for x,y in heap]

        