"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return True if not s else False

        first_match = bool(s) and (s[0] == p[0] or p[0] == '.')

        if len(p) >= 2 and p[1] == '*':
            # Case 1: '*' matches zero characters, so we skip it and the preceding character
            # Case 2: '*' matches one or more characters, so we try matching the remaining string with the same pattern
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            # No '*', just compare the first characters and continue with the remaining string and pattern
            return first_match and self.isMatch(s[1:], p[1:])


solution = Solution()
result = solution.isMatch('mississippi','mis*is*p*.')
print(result)
        