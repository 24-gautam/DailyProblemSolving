class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold , n , m = 0 , len(grid) , len(grid[0])

        for i in range(n) : 
            for j in range(m) : 
                if grid[i][j] : maxGold = max(maxGold , self.backtrack(grid , i , j , m , n)) 

        return maxGold 

    def backtrack(self, grid, i, j, m, n) : 
        res = 0 
        if n > i >= 0 and m > j >= 0 and grid[i][j] > 0 :
            prev = grid[i][j]
            grid[i][j] = -1 
            res = prev + max(res , self.backtrack(grid,i,j+1,m,n),self.backtrack(grid,i,j-1,m,n),self.backtrack(grid,i+1,j,m,n),self.backtrack(grid,i-1,j,m,n))
            grid[i][j] = prev 
        
        return res 
