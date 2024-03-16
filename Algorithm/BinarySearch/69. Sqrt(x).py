class Solution:
    def mySqrt(self, x: int) -> int:

        start = 0
        end = x
        while start <= end:
            mid = (end - start) // 2 + start 
            mid2 = mid * mid
            if mid2 == x:
                return mid
            elif mid2 > x:
                end = mid - 1
            else:
                start = mid + 1

        return end
solution = Solution() 
result = solution.mySqrt(10)
print(result)


        #. 8/2 = 4 
        # 4/2 = 2 
        # 2/2 = 1


        # 1,2,3,4.    ,5,6,7,8
        # 1,4,9.16
        