import heapq
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:

        # max heap
        # -1,-2,-3,-4
        # heap[0][0] 最大值

        ans = []
        count = defaultdict(int)
        maxHeap = []

        for num , fre in zip(nums , freq):
            count[num] += fre
            heapq.heappush(maxHeap , [-count[num] , num])

            while maxHeap and -maxHeap[0][0] != count[maxHeap[0][1]]:

                heapq.heappop(maxHeap)
            if maxHeap:
                ans.append(-maxHeap[0][0])
        return ans



        """ count = {}
        ans = []
        for num , fre in zip(nums , freq):
            if num not in count:
                new_fre = fre if fre >=0 else 0
                count[num] = new_fre

            else:
                new_fre = count[num] + fre if (count[num] + fre) >=0 else 0
                count[num] = new_fre

            ans.append(max(count.values()))
        return ans """
            
            
            

            

        