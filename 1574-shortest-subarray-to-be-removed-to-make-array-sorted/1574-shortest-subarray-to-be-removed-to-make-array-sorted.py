class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i , j = 0 , len(arr) - 1 

        while i < j and arr[i] <= arr[i+1] : i += 1 
        while j > 0 and arr[j-1] <= arr[j] : j -= 1 
        if j == 0 : return 0 

        res = min(len(arr) - i - 1 , j)

        while j < len(arr) : 
            k = self.search(arr[j] , arr , i)
            if k == -1 : 
                j += 1 
                continue 
            if j + 1 == len(arr) : res = min(res , j - k - 1)
            elif arr[j] <= arr[j+1] : 
                res = min(res , j - k - 1)
            else : return res 
            j += 1 
        
        return res



    
    def search(self, key , arr , high) : 
        low , res = 0 , -1

        while low <= high : 
            mid = low + (high - low) // 2 
            if arr[mid] <= key : 
                res = mid 
                low = mid + 1 
            else : 
                high = mid - 1 

        return res 