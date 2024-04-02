class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # map 
        map1 = {}
        map2 = {}

        for charS, charT in zip(s , t):
            if charS in map1:
                if map1[charS] != charT:
                    return False
            else:
                if charT in map2:
                    return False
                map1[charS] = charT
                map2[charT] = charS
        return True

        
        
        