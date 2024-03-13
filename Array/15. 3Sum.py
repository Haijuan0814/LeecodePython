class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        result = []
        processed = set()

        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1 
            
            while low < high :
                sum = nums[i] + nums[low] + nums[high]
                if sum == 0:
                    arr = [nums[i],nums[low],nums[high]]
                    
                    if str(arr) not in processed:
                        processed.add(str(arr))
                        result.append(arr)
                    low += 1
                    high -= 1
                elif sum > 0:
                    high -= 1
                else:
                    low +=1
                    #
        return result
    
solution = Solution() 
result = solution.threeSum([-1,0,1,0])
print(result)
        