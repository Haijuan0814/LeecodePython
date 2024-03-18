class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count = 0
        max_len = 0
        count_map = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count in count_map.keys():
                max_len = max(max_len , i - count_map[count])
            else:
                count_map[count] = i

        return max_len
        