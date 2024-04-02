class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        ans=float('-inf')
        preSum=[0]
        for ind,num in enumerate(nums):
            preSum.append(preSum[-1] + num)
            if num-k in freq:
                ans=max(ans,preSum[-1] - freq[num-k])
            if num+k in freq:
                ans=max(ans,preSum[-1] - freq[num+k])

            if num in freq:
                freq[num] = min(freq[num] , preSum[-1] - num)
            else:
                freq[num] = preSum[-1] - num
        return ans if ans!=float('-inf') else 0