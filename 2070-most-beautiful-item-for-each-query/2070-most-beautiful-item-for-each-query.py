class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x : x[0]) 

        for i in range(1 , len(items)) : 
            items[i][1] = max(items[i][1] , items[i-1][1])

        res = [] 

        for price in queries : 
            i = self.search(items , price) 
            res.append(0 if i == -1 else items[i][1])

        return res 



    def search(self, arr , key) : 
        low , high , res = 0 , len(arr) - 1 , -1

        while low <= high : 
            mid = low + (high - low) // 2 
            if arr[mid][0] <= key : 
                low = mid + 1 
                res = mid 
            else : 
                high = mid - 1 

        return res