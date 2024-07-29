class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res , dic = [] , [0] * 26 

        for c in words[0] : dic[ord(c) - 97] += 1

        for s in range(1 , len(words)) : 
            freq = [0] * 26 
            for c in words[s] : 
                freq[ord(c) - 97] += 1 
            
            for i in range(26) : 
                if freq[i] < dic[i] : dic[i] = freq[i] 
            
        for i in range(26) : 
            c = dic[i] 
            while c : 
                res.append(chr(i + 97)) 
                c -= 1 

        return res 
            