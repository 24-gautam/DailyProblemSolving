class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = nums[0] 

        if len(nums) == 1 : return 1 
        if nums[0] == 0 : return 0

        for i in range(1 , len(nums)) : 
            if i == len(nums) - 1 : return 1 
            mx -= 1 
            mx = max(mx , nums[i]) 
            if mx <= 0 : return 0

        return 1


