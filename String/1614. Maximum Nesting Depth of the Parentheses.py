class Solution:
    def maxDepth(self, s: str) -> int:

        cur_depth = 0
        max_depth = 0
        for c in s:
            if c =='(':
                cur_depth += 1
                max_depth = max(cur_depth , max_depth) 
            elif c == ')':
                cur_depth -= 1
        return max_depth


        