class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xorSum = 0 
        
        for i in range(1 << len(nums)) : 
            xor = 0
            for j in range(len(nums)) : 
                if i & 1 << j : xor ^= nums[j] 
            xorSum += xor 
        
        return xorSum 