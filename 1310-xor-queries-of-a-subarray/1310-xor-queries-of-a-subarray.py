class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for i in range(1 , len(arr)) : 
            arr[i] ^= arr[i-1] 

        for i , j in queries : 
            res.append(arr[j] ^ (0 if i == 0 else arr[i-1])) 
        
        return res 
