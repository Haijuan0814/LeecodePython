class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs) < 2:
            return len(pairs)

        # asc sort by the right number
        pairs = sorted(pairs , key = lambda x: x[1])
        count = 1
        right = pairs[0][1]
        for i in range(1,len(pairs)):
            if right < pairs[i][0]:
                right = pairs[i][1]
                count += 1
        return count


        """ heap = []
        heapq.heappush(heap , pairs[0])
        for i in range(1,len(pairs)):
            left , right = heapq.heappop(heap)
            if right < pairs[i][0]:
                heapq.heappush(heap,pairs[i])
                count += 1
            else:
                heapq.heappush(heap,[left,right])
        return count
 """                

        


        