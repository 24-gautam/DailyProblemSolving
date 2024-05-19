class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res , l , minCost , heapSum , i = [[wage[i] , quality[i]] for i in range(len(wage))] , [] , 2 ** 64 , 0 , 0

        def custom_key(item):
            return item[0] / item[1]

        res = sorted(res , key = custom_key)  

        for x , y in res : 
            heapSum += y
            if i < k : 
                i += 1 
                heapq.heappush(l , -y) 

            if i == k : 
                minCost = min(minCost , heapSum * x / y)
                heapSum , i = heapSum + heapq.heappop(l) , i - 1

        return minCost
                