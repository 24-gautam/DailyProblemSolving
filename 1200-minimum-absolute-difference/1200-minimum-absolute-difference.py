class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res , minDiff = [] , float('inf')
        arr.sort()

        for i in range(1, len(arr)) : 
            if arr[i] - arr[i-1] < minDiff : 
                minDiff = arr[i] - arr[i-1]
                res = [[arr[i-1], arr[i]]]
            elif arr[i] - arr[i-1] == minDiff : 
                res.append([arr[i-1], arr[i]])

        return res 