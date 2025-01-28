class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visit = [[0] * len(grid[0]) for i in grid] 
        res = 0
    
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if self.isValid(grid , i , j , visit) : 
                    res = max(res , self.bfs(grid , visit , i , j))

        return res 

    def bfs(self , grid , visit , i , j) : 
        q = deque([(i , j)]) 
        res = 0 

        while q : 
            n = len(q) 
            while n : 
                x , y = q.popleft() 
                res += grid[x][y]
                visit[x][y] = 1 
                cord = [[1,0],[-1,0],[0,-1],[0,1]] 

                for a , b in cord : 
                    if self.isValid(grid , x + a , y + b , visit) : 
                        q.append((x + a , y + b)) 
                
                n -= 1 
        
        return res

    def isValid(self , grid , r , c , visit) :
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] > 0 and not visit[r][c] 