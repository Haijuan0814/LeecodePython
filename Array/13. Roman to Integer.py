class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            num1 = mapping[s[i]]
            if i < len(s)-1:
                num2 = mapping[s[i+1]]
                if num1 >= num2:
                    result += num1
                else:
                    result -= num1
            else:
                result += num1
        return result
solution = Solution() 
result = solution.romanToInt("IX")
print(result)
        