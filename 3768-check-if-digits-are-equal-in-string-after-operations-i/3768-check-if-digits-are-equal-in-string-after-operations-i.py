class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(int , s)) 

        while len(s) > 2 : 
            i = 0 
            while i + 1 < len(s) : 
                s[i] = (s[i] + s[i+1]) % 10 
                i += 1 
            s.pop() 
        
        return s[0] == s[1]