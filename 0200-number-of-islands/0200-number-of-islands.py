class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands , dp = 0 , [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j] == '1' and not dp[i][j] : 
                    islands += 1
                    self.bfs(grid , i , j , dp)
        
        return islands 

    def bfs(self , grid , i , j , dp) : 
        if i == -1 or i == len(grid) or j == -1 or j == len(grid[0]) : return None 
        if dp[i][j] : return None 
        if grid[i][j] == '1' : 
            dp[i][j] = True 
            return self.bfs(grid , i + 1 , j , dp) or self.bfs(grid , i , j + 1 , dp) or self.bfs(grid , i , j - 1 , dp) or self.bfs(grid , i - 1 , j , dp)
