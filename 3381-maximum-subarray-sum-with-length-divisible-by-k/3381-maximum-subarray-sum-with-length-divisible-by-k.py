class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix, res = nums[::], float('-inf')

        for i in range(1, len(nums)) : 
            prefix[i] += prefix[i-1] 
        
        for i in range(k) : 
            s = 0 
            for j in range(k-1 + i, len(nums), k) : 
                s = max(s + prefix[j] - (prefix[j-k] if j - k >= 0 else 0), prefix[j] - (prefix[j-k] if j - k >= 0 else 0))
                res = max(res, s)

        return res