class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        def mergesort(nums , counts):
            if len(nums) == 1:
                return nums,counts
            stack = []
            mid = len(nums) // 2
            left, counts = mergesort(nums[: mid], counts)
            right, counts = mergesort(nums[mid :], counts)

            while left and right:
                if left[0] > right[0]:
                    counts[left[0][1]] += len(right) 
                    stack.append(left.pop(0))
                else:
                    stack.append(right.pop(0))
            stack.extend(left or right)  
            return stack, counts


        counts = [0] * len(nums)
        _nums = [(nums[index], index) for index in range(len(nums))] 
        stack, counts = mergesort(_nums, counts) 
        return counts