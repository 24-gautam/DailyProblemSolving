class Solution:
    def sortVowels(self, s: str) -> str:
        vowel , s = [] , list(s)
        for c in s : 
            if c in 'aeiouAEIOU' :
                vowel.append(c) 
        vowel.sort()
        
        k = 0 
        for i in range(len(s)) :
            if s[i] in 'aeiouAEIOU' :
                s[i] = vowel[k]
                k += 1 
        
        return "".join(s)