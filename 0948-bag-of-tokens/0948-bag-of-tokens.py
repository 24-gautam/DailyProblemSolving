class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i , j , score , maxScore = 0 , len(tokens) - 1 , 0 , 0
        tokens.sort()

        while i < len(tokens) and j >= 0 and i <= j and (score > 0 or power >= tokens[i]) : 
            if tokens[i] <= power : 
                score += 1 
                power -= tokens[i] 
                i += 1 
            else : 
                score -= 1 
                power += tokens[j] 
                j -= 1 

            maxScore = max(maxScore , score) 
        
        return maxScore 
