class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        idx = 0 
        res = 1

        for i in range(len(nums)) : 
            if nums[i] > nums[idx] : idx = i 

        i = idx
        cnt = 0 

        while i < len(nums) : 
            if nums[idx] == nums[i] : 
                cnt += 1 
            else : 
                cnt = 0 
            
            res = max(res , cnt) 
            i += 1 

        return res 
                
