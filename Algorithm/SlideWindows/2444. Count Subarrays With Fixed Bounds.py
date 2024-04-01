class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:

        left = 0
        count = 0
        minStart , maxStart = 0 , 0
        minFound , maxFound = False , False

        for right , num in enumerate(nums):
            if num > maxK or num < minK:
                left = right + 1
                minFound = False
                maxFound = False
            
            if num == minK:
                minStart = right
                minFound = True
                
            if num == maxK:
                maxStart = right
                maxFound = True

            if minFound and maxFound:
                print(nums[left:minStart+1])
                print(nums[left:maxStart+1])
                count += min(minStart , maxStart) - left + 1
        
        return count
    

solution = Solution()
print(solution.countSubarrays([928799,888361,928799,928799,928799,928799,124173,93094,399240,946505,93094,93094,585816] , 93094 , 928799))
        