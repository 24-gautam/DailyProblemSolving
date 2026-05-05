class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0 
        
        for i in range(len(nums)): 
            evenSet, oddSet = set(), set()
            for j in range(i, len(nums)): 
                if nums[j] & 1 == 1 : 
                    oddSet.add(nums[j])
                else : evenSet.add(nums[j]) 
                if len(evenSet) == len(oddSet) : 
                    res = max(res, j + 1 - i) 

        return res