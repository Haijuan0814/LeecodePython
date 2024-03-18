class NumArray:

    def __init__(self, nums: List[int]):
        #self.nums = nums

        arr = [nums[0]]
        for i in range(1, len(nums)):
            arr.append(arr[-1] + nums[i])
        self.arr = arr

    def sumRange(self, left: int, right: int) -> int:
        if left == 0 :
            return self.arr[right]
        else:
            return self.arr[right] - self.arr[left - 1]


        """ new_nums = self.nums[left:right+1]
        _sum = 0
        for num in new_nums:
            _sum += num
        return _sum """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)