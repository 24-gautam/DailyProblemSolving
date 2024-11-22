class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[-1] * n for i in range(m)] 

        for x , y in guards : grid[x][y] = 1 
        for x , y in walls : grid[x][y] = 2  

        for x , y in guards : 
            i = x + 1 
            while i < m and grid[i][y] != 1 and grid[i][y] != 2 : 
                grid[i][y] , i = 0 , i + 1 

            i = x - 1 
            while i >= 0 and grid[i][y] != 1 and grid[i][y] != 2 :
                grid[i][y] , i = 0 , i - 1 

            j = y + 1 
            while j < n and grid[x][j] != 1 and grid[x][j] != 2 : 
                grid[x][j] , j = 0 , j + 1 
            
            j = y - 1 
            while j >= 0 and grid[x][j] != 1 and grid[x][j] != 2 : 
                grid[x][j] , j = 0 , j - 1 

        res = 0 

        for i in grid : 
            for j in i :
                if j == -1 : res += 1 

        return res

        
        