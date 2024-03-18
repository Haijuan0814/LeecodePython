import functools
class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        def compare(n1 , n2):
            if int(n1 + n2) > int(n2 + n1):
                return -1
            else:
                return 1
        # 将比较函数转换为 key 函数
        key_func = functools.cmp_to_key(compare)
        print(key_func)

        for i,num in enumerate(nums):
            nums[i] = str(num)
        
        nums = sorted(nums, key = key_func)
        return ''.join(nums) if nums[0] != '0' else '0'
        
        
        """ nums = sorted(nums , key = lambda x : str(x), reverse = True)
        s = ''
        for num in nums:
            s = s + str(num)
        return s """

        

solution = Solution() 
result = solution.largestNumber([12,2,4,5,9,0])

        

        