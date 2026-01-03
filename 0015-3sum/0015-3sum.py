class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = list()
        i , j , k = 0 , 0 , 0

        while i < len(nums) - 2 : 
            j , k , target = i + 1 , len(nums) - 1 , -nums[i] 
            
            while j < k : 
                s = nums[j] + nums[k]
                if target > s : j += 1 
                elif target < s : k -= 1 
                else : 
                    res.append([nums[i], nums[j], nums[k]])
                    x, y = nums[j] , nums[k]
                    while j < k and nums[j] == x : j += 1 
                    while j < k and nums[k] == x : k -= 1 
            i += 1 
            while i < len(nums) and nums[i] == nums[i-1] : i += 1 

        return res 
