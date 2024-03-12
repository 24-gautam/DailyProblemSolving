class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic , res = defaultdict(int) , ''
        for c in s : dic[c] += 1 

        for i in order : 
            if i in dic : 
                res += i * dic[i] 
                dic[i] = 0 
        
        for key , val in dic.items() : 
            if val != 0 : res += key * val 
        
        return res 

