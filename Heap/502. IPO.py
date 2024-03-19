import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:

        if w < min(capital) or k == 0:
            return 0

        cando = []
        last = []

        for i in range(len(profits)):
            pure_profit = profits[i]
            if capital[i] <= w:
                heapq.heappush(cando , -profits[i] )
            else:
                heapq.heappush(last , (capital[i],-profits[i]))
                
        while k >0 and cando:
            k -= 1
            w += -heapq.heappop(cando)
            
            while last:
                c , p = heapq.heappop(last)
                if w >= c:
                    heapq.heappush(cando , p)
                else:
                    heapq.heappush(last , (c,p))
                    break
        return w

        