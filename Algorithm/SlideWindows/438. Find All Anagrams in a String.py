
# fixed window size
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(p)
        n2 = len(s)
        if n1 > n2:
            return []
        
        left = 0
        res = []
        p = sorted(p)

        for right in range(n1 , n2+1):
            if sorted(s[left:right]) == p:
                res.append(left)
            left += 1
        return res
        