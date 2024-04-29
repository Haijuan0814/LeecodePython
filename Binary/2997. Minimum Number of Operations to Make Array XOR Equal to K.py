class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        ans = 0
        for i in nums :
            ans ^= i
        
        ans = ans ^ k
        n = 0
        for b in bin(ans):
            if b == '1':
                n += 1
        return n
        