class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        # The condition required: a+b > c
        n = len(nums)
        if n < 3 : return 0

        nums = sorted(nums)
        count = 0

        for i in range(2 , n):
            low = 0
            high = i-1

            while low < high:
                if nums[low] + nums[high] > nums[i]:
                    # low 都符合要求，那么 把low换成low～high之间的也一定符合要求
                    count += high - low
                    high -= 1
                else:
                    low += 1
        return count

