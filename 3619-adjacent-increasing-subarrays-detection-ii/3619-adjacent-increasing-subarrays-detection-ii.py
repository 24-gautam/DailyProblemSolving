class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev, k, res = 0 , 1 , 0 

        for i in range(1 , len(nums)) : 
            if nums[i] > nums[i-1] : k += 1 
            else : prev , k = k , 1 
            
            res = max(res , k // 2 , min(k , prev))

        return res 