class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res , patternFreq = 0 , defaultdict(int) 

        for row in matrix : 
            t = tuple() 
            for i in range(len(row) - 1) : 
                if row[i] != row[i+1] : t = t + (i ,) 
            t = t + (len(row) , ) 
            patternFreq[t] += 1 
            res = max(res , patternFreq[t])  
        
        return res 

