class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t , res = tickets[k] , 0 

        for i in range(k + 1) : res += min(t , tickets[i]) 
        for i in range(k + 1 , len(tickets)) : 
            if tickets[i] >= t : res += t - 1 
            else : res += min(t , tickets[i])
    
        return res
