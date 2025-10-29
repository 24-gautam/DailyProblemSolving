class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        c , n = 0 , sum(nums)

        for i in range(len(nums)) : 
            prev = 0 if i == 0 else nums[i-1]
            if nums[i] == 0: 
                if n == 2 * prev : c += 2 
                elif n - 1 == 2 * prev or n + 1 == 2 * prev : c += 1
                
            if i > 0 : nums[i] += nums[i-1] 
            
        return c 
