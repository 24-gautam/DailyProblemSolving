class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        res , oneCnt , currOneCnt , i , n = 1e9 , nums.count(1) , 0 , 0 , len(nums)

        while i < 2 * len(nums) : 
            if i < oneCnt : currOneCnt += 1 if nums[i] == 1 else 0
            elif nums[i%n] == 1 : 
                currOneCnt += 1 if nums[(i-oneCnt) % n] == 0 else 0 
            else : 
                currOneCnt += -1 if nums[(i-oneCnt) % n] == 1 else 0 
            
            res = min(res , oneCnt - currOneCnt) 
            i += 1 
        
        return res 



        