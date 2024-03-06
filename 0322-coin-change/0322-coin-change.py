class Solution:
    dp = []
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [[-1 for i in range(amount + 1)] for j in range(len(coins))] 
        res = self.solve(coins , amount , 0)
        return -1 if res >= 1e9 else res

    def solve(self , coins , amount , i) : 
        if i == len(coins) or amount < 0 : return 1e9 
        if amount == 0 : return 0 
        if self.dp[i][amount] != -1 : return self.dp[i][amount] 
        take = 1e9
        if coins[i] <= amount : take = 1 + min(self.solve(coins , amount - coins[i] , i + 1) , self.solve(coins , amount - coins[i] , i)) 
        skip = self.solve(coins , amount , i + 1) 
        self.dp[i][amount] = min(take, skip) 
        return self.dp[i][amount]