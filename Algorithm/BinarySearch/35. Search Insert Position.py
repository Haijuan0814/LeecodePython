class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0

        start = 0
        end = len(nums)-1
        while start <= end:
            half = (end - start) // 2 + start
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            elif nums[half] == target:
                return half
            elif nums[half] < target:
                start = half + 1
            else:
                end = half - 1

        return start
    
solution = Solution() 
result = solution.searchInsert([-1,0,3,5,9,12],8)
print(result)