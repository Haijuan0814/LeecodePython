class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        most_freq = 0
        chars_count = defaultdict(list)
        left = 0
        max_len = 0
        
        for right , c in enumerate(s):
            chars_count[c] = chars_count.get(c , 0) + 1 
            most_freq = max(most_freq , chars_count[c])

            if right - left + 1 > most_freq + k:
                chars_count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

        