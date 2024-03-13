""" Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321 """

class Solution:
    def reverse(self, x: int) -> int:

        reverse = int(str(abs(x))[::-1])
        result = reverse if x > 0 else reverse * (-1)
        return result if -2**31 <= result <= 2**31-1 else 0
        """ 
        if x > 0:
            _x = str(x)
            reverse = _x[::-1]
            return int(reverse) if int(reverse) <= pow(2,31)-1 else 0
        elif x == 0:
            return x
        else:
            _x = str(x)
            _x = _x.replace('-','')
            reverse = _x[::-1]
            reverse = 0 - int(reverse)
            return reverse if reverse >= pow(-2,31) else 0 
    """        

solution = Solution()
result = solution.reverse(-123)
print(result)
        