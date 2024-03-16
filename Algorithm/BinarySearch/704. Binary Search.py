class Solution:
    def search(self, nums: list[int], target: int) -> int:

        if not nums:
            return -1

        length = len(nums)
        end = length-1
        start = 0


        while start <= end :
            half = (end - start) // 2 + start
            mid = nums[half]
            if mid == target:
                return half
            elif mid > target:
                end = half - 1
            else:
                start = half + 1


        return -1
    
solution = Solution() 
result = solution.search([-1,0,3,5,9,12,13],9)
print(result)

        