class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        _max = max(nums)
        count = defaultdict(int)
        res = 0
        for right , num in enumerate(nums):
            count[num] += 1

            while count[_max] >= k:
                res +=  n - right
                count[nums[left]] -= 1
                left += 1
        
        return res


        