
#
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Solution:算法，字符串&数组; 双指针，滑动窗口
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        read = {}
        left = 0
        maxLength = 0
        for right , x in enumerate(s):
            if x not in read:
                currentLength = right - left + 1
                maxLength = max(maxLength , currentLength) 
            else:
                x_index = read[x]
                if(x_index < left):
                    maxLength = max(maxLength , right - left +1)
                else: 
                    left = read[x]+1 
            read[x] = right
        return maxLength




        
