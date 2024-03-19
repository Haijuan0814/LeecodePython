class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        sort = sorted(nums)
        left = 0
        right = len(nums) - 1
        isStart = isEnd = False

        if len(nums) == 1 or sort == nums:
            return 0

        for x in range(len(nums)):
            if sort[left] == nums[left]:
                left += 1
            if sort[right] == nums[right]:
                right -= 1
            if left == right:
                return 0
        return right - left + 1