class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currTime , res = customers[0][0] , 0

        for i , j in customers : 
            if i > currTime : 
                res += j
                currTime = i + j
            else : 
                res += currTime + j - i
                currTime += j
        
        return res / len(customers)