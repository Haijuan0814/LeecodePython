class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) is 0:
            return ""
        
        prefix = ''
        strs.sort()
        for i in range(len(strs[0])):
            first = strs[0]
            last = strs[-1]
            if first[i] == last[i]:
                prefix += first[i]
            else:
                return prefix
        return prefix

        