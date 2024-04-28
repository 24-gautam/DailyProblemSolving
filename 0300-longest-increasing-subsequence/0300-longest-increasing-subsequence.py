class Solution:
    dp = []
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.dp = [[-1 for i in range(len(nums) + 1)] for j in range(len(nums) + 1)] 
        return self.solve(nums , 0 , -1) 
    
    def solve(self, nums, i, j) : 
        if i == len(nums) : return 0 
        if j != -1 and self.dp[i][j] != -1 : return self.dp[i][j]
        take = 0
        if j == -1 or nums[i] > nums[j] : take = 1 + self.solve(nums , i + 1 , i) 
        skip = self.solve(nums , i + 1 , j)

        if j == -1 : return max(take , skip) 
        else : self.dp[i][j] = max(take , skip) 

        return self.dp[i][j]