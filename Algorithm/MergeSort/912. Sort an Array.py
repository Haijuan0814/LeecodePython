class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def mergrSort(arr):
            if len(arr) <= 1:
                return arr
            
            # 分割数组
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            
            # 递归地对左右子数组进行排序
            left_half = mergrSort(left_half)
            right_half = mergrSort(right_half)
            
            # 合并已排序的子数组
            return merge(left_half, right_half)
        
        c = 1
        def merge(left , right):
            merged = []
            left_index , right_index = 0 , 0
            nonlocal c
            print(c)
            #print(merged)
            #print(right)
            
            c += 1
            
            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1

            # 将剩余元素添加到合并数组中
            merged.extend(left[left_index:])
            merged.extend(right[right_index:])
            print(merged)
            return merged
           

       
        #arr = [38, 27, 43, 3, 9, 82, 10,10,10]
        mergrSort(nums)
    
solution = Solution()
solution.sortArray([38, 27, 43, 3, 9, 82, 10,10,10])

# 38, 27, 43, 3        9, 82, 10,10,10
# 38, 27    ,         43, 3 


# 3 27 38 43      9, 10,10,10,,82,



            
        