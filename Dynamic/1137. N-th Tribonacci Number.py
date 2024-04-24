class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2 :
            return n
        
        dp = [0 , 1 , 1]

        for i in range(3 , n+1):
            summ = dp[0] + dp[1] + dp[2]
            dp[0] , dp[1] , dp[2] = dp[1] , dp[2] , summ

        return dp[2]

        