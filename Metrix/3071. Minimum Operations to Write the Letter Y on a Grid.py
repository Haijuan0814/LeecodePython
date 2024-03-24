class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        

        n = len(grid)
        mid = (n - 1) / 2
        y = []
        non_y = []
        for i in range(n):
            for j in range(n):
                x = grid[i][j]
                if j <= mid and i == j:
                    y.append(x)
                elif j == mid and i > mid:
                    y.append(x)
                elif j > mid and i+j == n-1:
                    y.append(x)
                else:
                    non_y.append(x)

        c1 = Counter(y)
        c2= Counter(non_y)
        
        if len(c1) == 1 and len(c2) == 1 and c1.keys() == c2.keys():
            return len(y)
        maxOp = 0
        for i in c1:
            for j in c2:
                if i != j:
                    temp = c1[i] + c2[j]
                    maxOp = max(maxOp , temp)
        return n**2 - maxOp

        # Counter({4: 4, 3: 3, 2: 2, 1: 1})
        """ counter_y = Counter(y)
        counter_non_y= Counter(non_y)
        common_y = counter_y.most_common()
        counter_non_y = counter_non_y.most_common()
    
        if common_y[0][0] != counter_non_y[0][0]:
            return n*n - common_y[0][1] - counter_non_y[0][1]
        elif  len(common_y) == 1 and  len(counter_non_y) == 1:
            return common_y[0][1]
        elif len(common_y) == 1:
            return n*n - common_y[0][1] - counter_non_y[1][1]
        elif len(counter_non_y) == 1:
            return n*n - common_y[1][1] - counter_non_y[0][1]
        else:
            n1 = n*n - common_y[0][1] - counter_non_y[1][1]
            n2 = n*n - common_y[1][1] - counter_non_y[0][1]
            return min(n1 , n2)
        

 """