class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, right, down, left = 0 , len(matrix[0]) - 1 , len(matrix) - 1 , 0 
        n = len(matrix) * len(matrix[0]) 
        res = []

        while left <= right and up <= down : 
            i = left
            while i <= right and n :
                res.append(matrix[up][i]) 
                i += 1 
                n -= 1

            up += 1 
            i = up 

            while i <= down and n :
                res.append(matrix[i][right]) 
                i += 1 
                n -= 1 
            
            right -= 1 
            i = right 

            while i >= left and n: 
                res.append(matrix[down][i]) 
                i -= 1 
                n -= 1

            down -= 1 
            i = down 

            while i >= up and n : 
                res.append(matrix[i][left]) 
                i -= 1 
                n -= 1

            left += 1 
        
        return res