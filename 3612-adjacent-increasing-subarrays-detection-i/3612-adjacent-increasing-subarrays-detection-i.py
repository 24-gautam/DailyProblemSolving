class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 2 * k + 1) : 
            if self.isStrictlyIncreasing(nums, i, i + k) and self.isStrictlyIncreasing(nums, i + k, i + 2 * k) : return True 

        return False
    

    def isStrictlyIncreasing(self, nums: List[int], i: int, k:int) -> bool: 
        while i + 1 < k : 
            if nums[i + 1] <= nums[i] : return False
            i += 1 
        
        return True