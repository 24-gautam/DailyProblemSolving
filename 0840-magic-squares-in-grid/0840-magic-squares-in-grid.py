class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0 

        for i in range(len(grid) - 2) : 
            for j in range(len(grid[0]) - 2) : 
                res += self.isMagicSquare(grid, i , j)

        return res  
        

    def isMagicSquare(self,grid , i , j) : 
        row = [sum(grid[k][l] for l in range(j , j + 3)) for k in range(i , i + 3)] 
        col = [sum(grid[l][k] for l in range(i , i + 3)) for k in range(j , j + 3)]
        dia = [grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] , grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]]
        n = set(grid[n][m] for n in range(i , i + 3) for m in range(j , j + 3))
        haveCommon = bool({10,11,12,13,14,15} & n)

        return 1 if row[0] == row[1] == row[2] == col[0] == col[1] == col[2] == dia[0] == dia[1] and len(n) == 9 and not haveCommon else 0 