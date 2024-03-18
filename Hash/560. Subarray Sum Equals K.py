class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        curSum = 0
        count = 0
        prevSums = {0:1}
        for num in nums:
            curSum += num
            if curSum - k in prevSums:
                count += prevSums[curSum - k]
            if curSum in prevSums:
                prevSums[curSum] += 1
            else:
                prevSums[curSum] = 1

        return count

       
        

