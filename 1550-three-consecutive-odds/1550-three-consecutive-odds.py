class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(2 , len(arr)) : 
            if arr[i] * arr[i-1] * arr[i-2] % 2 == 1 : 
                return True 

        return False