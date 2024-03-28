class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        left = 0
        maxQueue = deque() # 从大到小
        minQueue = deque() # 从小到大

        for right , num in enumerate(nums):
            while maxQueue and maxQueue[-1] < num:
                maxQueue.pop()
            while minQueue and minQueue[-1] > num:
                minQueue.pop()
            maxQueue.append(num)
            minQueue.append(num)

            if maxQueue[0] - minQueue[0] > limit:
                leftVal = nums[left]
                if maxQueue[0] == leftVal:
                    maxQueue.popleft()
                if minQueue[0] == leftVal:
                    minQueue.popleft()
                left += 1
        return len(nums) - left

        


        