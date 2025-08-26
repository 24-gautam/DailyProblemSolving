class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        i , maxDiag = 0 , 0 

        for idx, (l , b) in enumerate(dimensions) : 
            diag = l*l + b*b
            if diag > maxDiag : maxDiag , i = diag , idx 
            elif diag == maxDiag and dimensions[i][1] * dimensions[i][0] < l * b : i = idx

        return dimensions[i][1] * dimensions[i][0]