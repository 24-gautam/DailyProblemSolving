class Solution:
    def minimumLength(self, s: str) -> int:
        i , j = 0 , len(s) - 1 

        while i < j : 
            if s[i] != s[j] : return j - i + 1 
            c = s[i] 
            while i < len(s) and s[i] == c : i += 1 
            while j >= 0 and s[j] == c : j -= 1 
        
        return 1 if i == j else 0 