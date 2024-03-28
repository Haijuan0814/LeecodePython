class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefixSumCount = defaultdict(int)
        prefixSum = 0
        count = 0

        for i in range(len(nums)):
            
            prefixSum += nums[i]
            
            if prefixSum == goal:
                count += 1
            count += prefixSumCount[prefixSum - goal]
            prefixSumCount[prefixSum] += 1

        return count
            