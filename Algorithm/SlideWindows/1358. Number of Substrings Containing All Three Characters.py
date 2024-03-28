class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 字符串至少分别出现一次 a/b/c

        count = 0
        left = 0
        n = len(s)
        #occur = {'a':0 , 'b':0 , 'c':0}
        occur = defaultdict(int)
        for right , char in enumerate(s):
            occur[char] += 1
            while len(occur) == 3:
                occur[s[left]] -= 1
                if occur[s[left]] == 0:
                    del occur[s[left]]

                count += n - right
                left += 1
                

        return count



        