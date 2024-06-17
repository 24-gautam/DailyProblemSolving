class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i , j = 0 , int(math.sqrt(c))

        while i <= j :
            if i * i + j * j == c : return True 
            if i * i + j * j < c : i += 1 
            else : j -= 1 
        
        return False 