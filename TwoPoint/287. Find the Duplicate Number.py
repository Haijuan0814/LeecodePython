class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums.sort()
        i = 0
        j = len(nums)-1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < (mid + 1):
                j = mid
            else:
                i = mid + 1
        return nums[i]
        