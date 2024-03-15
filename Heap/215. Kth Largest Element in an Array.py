import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        # min-heap : parent > child
        # max-heap : parent < child
        if not nums:
            return None
        if k<1:
            return None
        heap = []
        heapq.heapify(heap)
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        x = heapq.heappop(heap)
        return x

       
                
       
solution = Solution()
result = solution.findKthLargest([1,2,5,4],2)
print(result)
        