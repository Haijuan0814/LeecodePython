class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums =set(nums)
        i = 1
        while(1):
            if i not in nums:
                return i
            i += 1

        
solution = Solution() 
result = solution.firstMissingPositive([2,1,0])
print(result)