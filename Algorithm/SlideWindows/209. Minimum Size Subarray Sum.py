class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        total = sum(nums)

        if total < target:
            return 0
     
        minLength = float(inf)
        _sum = 0
        left = 0
        for right,num in enumerate(nums):
            _sum += num
            while _sum >= target:
                _sum -= nums[left]
                minLength = min(minLength , right - left + 1)
                left += 1
        
        return minLength

