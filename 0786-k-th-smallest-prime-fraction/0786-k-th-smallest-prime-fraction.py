class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        q , res = [] , []
        
        for i in range(len(arr)) : 
            for j in range(i + 1 , len(arr)) : 
                heapq.heappush(q , (arr[i] / arr[j] , arr[i] , arr[j])) 

        while k : 
            node = heapq.heappop(q) 
            res = [node[1] , node[2]]
            k -= 1 
        
        return res