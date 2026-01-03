class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = up = down = 0

        for i in range(len(arr) - 1) : 
            if down and arr[i] < arr[i+1] or arr[i] == arr[i+1] : up = down = 0 
            up += arr[i] < arr[i+1] 
            down += arr[i] > arr[i+1] 
            if up and down : res = max(res, up + down + 1) 

        return res
