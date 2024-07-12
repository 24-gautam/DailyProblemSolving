class Solution:
    def bulbSwitch(self, n: int) -> int:
        i , res = 1 , 0
        
        while i * i <= n : i , res = i + 1 , res + 1 

        return res 