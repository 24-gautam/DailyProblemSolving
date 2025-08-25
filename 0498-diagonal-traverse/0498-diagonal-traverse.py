class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up , res = True , []
        i , j = 0 , 0 
        m , n = len(mat) , len(mat[0]) 

        while True : 
            res.append(mat[i][j])
            if i == m - 1 and j == n - 1 : break
            if up : 
                i -= 1 
                j += 1 
                if i == -1 and j < n : i , up = 0 , False
                elif j == n : i , j , up = i + 2 , j - 1 , False
            else : 
                i += 1 
                j -= 1 
                if j == -1 and i < m : j , up = 0 , True 
                elif i == m : i , j , up = i - 1 , j + 2 , True

        return res 
                

