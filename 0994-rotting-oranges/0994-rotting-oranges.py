class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q , rotten , fresh , visit , res = deque() , 0 , 0 , set() , 0

        for i in range(len(grid)) : 
            for j in range(len(grid[i])) :
                if grid[i][j] == 1 : fresh += 1 
                if grid[i][j] == 2 :
                     rotten += 1 
                     q.append((i , j)) 

        if fresh == 0 : return 0
        total = rotten + fresh  

        while q : 
            n , res = len(q) , res + 1
            while n : 
                i , j = q.popleft() 
                visit.add((i , j)) 

                if (i + 1 , j) not in visit and self.valid(grid , i + 1 , j) : 
                    q.append((i + 1 , j))
                    rotten += 1
                if (i - 1 , j) not in visit and self.valid(grid , i - 1 , j) : 
                    rotten += 1
                    q.append((i - 1 , j))
                if (i , j + 1) not in visit and self.valid(grid , i , j + 1) : 
                    rotten += 1
                    q.append((i , j + 1))
                if (i , j - 1) not in visit and self.valid(grid , i , j - 1) : 
                    rotten += 1
                    q.append((i , j - 1))    

                n -= 1
        return -1 if rotten < total else res - 1 

    def valid(self , grid , i , j) : 
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == 1 :
            print(i,j) 
            grid[i][j] = 2 
            return True 
        return False