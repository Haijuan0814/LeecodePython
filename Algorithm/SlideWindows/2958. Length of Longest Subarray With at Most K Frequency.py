class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        left = 0
        occur = defaultdict(int)
        maxLength = 1
        for right , num in enumerate(nums):
            occur[num] += 1
            while occur[num] > k:
                leftVal = nums[left]
                #maxLength = max(maxLength , right-left)
                occur[leftVal] -= 1
                left += 1
                
            maxLength = max(maxLength , right-left+1)
        
        return maxLength
        