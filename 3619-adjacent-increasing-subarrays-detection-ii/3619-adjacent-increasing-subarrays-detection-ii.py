class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        maxIncSubArr , k = [1] * len(nums) , 1

        for i in range(len(nums) - 2, -1, -1) : 
            if nums[i+1] > nums[i] : maxIncSubArr[i] += maxIncSubArr[i+1] 
        
        low , high = 0 , len(nums) // 2 

        print(maxIncSubArr)

        while low <= high : 
            mid = low + (high - low) // 2 

            if self.isValid(maxIncSubArr, mid) : 
                k = mid
                low = mid + 1 
            else : 
                high = mid - 1 
        
        return k
    
    def isValid(self, nums, k) : 
        for i in range(len(nums) - 2 * k + 1) : 
            if nums[i] >= k and nums[i+k] >= k : return True 

        return False 