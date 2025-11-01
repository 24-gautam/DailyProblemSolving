class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq , res = [0] * (max(nums) + k + 1) , 0

        for i in nums : freq[i] += 1 

        for i in range(1, max(nums) + k + 1) : 
            freq[i] += freq[i-1] 

        for i in range(max(nums) + 1) : 
            left = max(0, i - k) 
            right = i + k 
            curr = freq[i] - (freq[i-1] if i else 0)
            total = freq[right] - (freq[left-1] if left else 0) 
            # print('i =', i, curr, total)
            res = max(res, curr + min(numOperations, total - curr)) 

        return res