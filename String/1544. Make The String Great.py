class Solution:
    def makeGood(self, s: str) -> str:

        n = len(s)
        if n < 2:
            return s
        
        s1 = s
        index = 0
        while index < len(s1) - 1:
            if abs(ord(s1[index]) - ord(s1[index+1])) == 32:
                s1 = s1[:index] + s1[index+2:]
                if index != 0:
                    index -= 1
            else:
                index += 1
        return s1
                   