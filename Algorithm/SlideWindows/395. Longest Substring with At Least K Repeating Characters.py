class Solution:
    def longestSubstring(self, s: str, k: int) -> int:



        
        if len(s) < k:
            return 0
        
        char_freq = {}
        for char in s:
            if char not in char_freq:
                char_freq[char] = 1
            else:
                char_freq[char] += 1

        for i , char in enumerate(s):
            if char_freq[char] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left , right)
        return len(s)


     


        