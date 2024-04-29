class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor , res = 0 , 0 
        for i in nums : xor ^= i 
        
        while xor > 0 or k > 0 : 
            if k & 1 != xor & 1 : res += 1 
            k >>= 1 
            xor >>= 1 
        
        return res 