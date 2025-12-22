class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res , prev = 0 , [0] * len(strs) 

        for i in range(len(strs[0])) : 
            j = 1 
            while j < len(strs) : 
                if not prev[j] and strs[j][i] < strs[j-1][i] : 
                    res += 1 
                    break 
                j += 1
                
            if j < len(strs): continue 

            for j in range(1 , len(strs)) : 
                prev[j] |= strs[j][i] > strs[j-1][i] 

        return res 