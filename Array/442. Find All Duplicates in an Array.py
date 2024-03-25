class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []
        res = set()
        visited = set()
        for i in nums:
            if i not in visited:
                visited.add(i)
            else:
                res.add(i)
        return res

        