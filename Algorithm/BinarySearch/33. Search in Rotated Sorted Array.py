
""" 
二分搜索（Binary Search）是一种在已排序数组中查找目标值的搜索算法。该算法通过重复将目标值与数组中间元素进行比较，并根据比较结果缩小搜索范围，直到找到目标值或确定目标值不存在为止。

基本思想是首先将数组的中间元素与目标值进行比较，如果中间元素等于目标值，则搜索成功；如果中间元素大于目标值，则在数组的左半部分继续搜索；如果中间元素小于目标值，则在数组的右半部分继续搜索。通过每次比较后将搜索范围缩小一半，直到找到目标值或搜索范围为空为止。

二分搜索的时间复杂度为 O(log n)，其中 n 是数组的长度。这使得二分搜索成为一种高效的搜索算法，特别适用于大型已排序数组的查找操作。 """

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        start = 0
        end = len(nums)-1
        while start <= end :

            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            elif nums[start] < nums[end]:
                # binary search
                half = (end - start) // 2 + start
                mid = nums[half]
                if mid == target:
                    return half
                elif mid > target:
                    end = half - 1
                else:
                    start = half + 1
            else:
                start += 1
                end -= 1
        return -1
        