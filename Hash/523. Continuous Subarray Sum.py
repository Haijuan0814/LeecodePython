class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        curSum = 0
        preSums = []
        for num in nums:
            curSum += num
            preSums.append(curSum % k)
        
        visited = {}
        for index , val in enumerate(preSums):
            if val == 0 and index > 0:
                return True
            if val in visited.keys():
                if index - visited[val] > 1:
                    return True
            else:
                visited[val] = index
        return False