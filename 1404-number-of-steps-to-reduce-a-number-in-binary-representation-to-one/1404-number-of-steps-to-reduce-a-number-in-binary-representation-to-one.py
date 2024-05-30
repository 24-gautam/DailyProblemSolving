class Solution:
    def numSteps(self, s: str) -> int:
        res , i , carry = 0 , len(s) - 1 , 0

        while i > 0 : 
            if s[i] == '1' and carry == 0 : 
                carry , res = 1 , res + 2
            elif s[i] == '1' and carry == 1 : 
                res += 1 
            elif s[i] == '0' and carry == 1 : 
                res += 2 
            else : res += 1 
            i -= 1
            
        return res + 1 if carry == 1 else res