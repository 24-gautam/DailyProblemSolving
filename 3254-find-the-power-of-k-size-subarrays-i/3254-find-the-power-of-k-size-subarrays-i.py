class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1 : return nums

        res , i , j = [] , 1 , -1

        while i < len(nums) : 
            if nums[i] != nums[i-1] + 1 : j = i
            if i >= k - 1 : 
                # print(j , i - k + 1 , i)
                if i - k + 1 < j <= i : res.append(-1) 
                else : 
                    res.append(nums[i])
            i += 1 

        return res 
