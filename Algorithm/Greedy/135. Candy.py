class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        if n <= 1:
            return n

        candies = [1] * n
        # first loop: check from left to right
        for i in range(1,n):
            if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
                candies[i] = candies[i-1] + 1
        # second loop: check from right to left
        for j in range(n-2 , -1 , -1):
            if ratings[j+1] < ratings[j] and candies[j+1] >= candies[j]:
                candies[j] = candies[j+1] + 1
        
        return sum(candies)

        

        