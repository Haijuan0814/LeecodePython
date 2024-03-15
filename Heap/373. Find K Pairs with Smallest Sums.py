class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        ## num 都是递增的，所以越往后越大
        ## 找最小的，利用最小堆
        n1 = len(nums1)
        n2 = len(nums2)
        if k == 0 or n1 == 0 or n2 == 0:
            return []
        if k == 1:
            return [[ nums1[0] , nums2[0]]]

        heap = []
        heapq.heappush(heap,(nums1[0] + nums2[0],0,0) )
        visited = set()
        visited.add((0,0))
        res = []
        while k and heap:
            _,i,j = heapq.heappop(heap)
            res.append([nums1[i] , nums2[j]])

            if i+1 < n1 and (i+1,j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j],i+1,j))
                visited.add((i+1,j))
            
            if j+1 < n2 and (i,j+1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j+1],i,j+1))
                visited.add((i,j+1))
            
            k = k - 1

        return res
