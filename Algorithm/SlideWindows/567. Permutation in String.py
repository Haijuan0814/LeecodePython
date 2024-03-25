class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 , n2 = len(s1),len(s2)
        # solution-1, using counter
        c1 , c2 = Counter(s1) , Counter(s2[:n1])

        # for s1 & s2, the no. of having same no. of a character
        equal_count = 0
        for c in c1:
            equal_count += (c1[c] == c2[c])
        
        for i in range(n1 , n2):
            if equal_count == len(c1): 
                return True

            # right char
            right = s2[i]
            if c1[right] and c1[right] == c2[right]: equal_count -= 1
            c2[right] += 1  
            if c1[right] and c1[right] == c2[right]: equal_count += 1

            # left char
            left = s2[i-n1]
            if c1[left] and c1[left] == c2[left]: equal_count -= 1
            c2[left] -= 1
            if c1[left] and c1[left] == c2[left]: equal_count += 1

        return equal_count == len(c1)


        # solution-2, not efficient
        """ if n1 > n2:
            return False

        # fixed window size
        # window_size = n1
        for i in range(n2 - n1 + 1):
            s = s2[i:i+n1]
            if sorted(s) == sorted(s1):
                return True
        return False """
            
        