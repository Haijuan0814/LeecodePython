class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        length = len(matrix)
        start = 0
        end = length-1
        while start <= end:
            half = (end - start) // 2 + start
            midMetrix = matrix[half]
            if target in midMetrix:
                return True
            
            if midMetrix[0] > target:
                end = half - 1
            elif midMetrix[-1] < target:
                start = half + 1
            else:
                return False