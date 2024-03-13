""" Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer. """


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = {}
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j][::-1] == s[i:j]:
                    result[s[i:j]]=len(s[i:j])
                    
        # 返回字典result中value最大值对应的key
        longest = max(result,key = result.get)
        return longest
        
            

        