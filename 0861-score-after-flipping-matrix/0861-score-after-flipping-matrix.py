class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        score , k = n * 2 ** (m - 1) , m - 1

        for i in range(n) : 
            if not grid[i][0] : 
                for j in range(m) : 
                    grid[i][j] ^= 1 
        
        for i in range(1 , m) : 
            zeroCnt , k = 0 , k - 1
            for j in range(n) : 
                if not grid[j][i] : zeroCnt += 1 
            
            if zeroCnt > n // 2 : score += zeroCnt * 2 ** k
            else : score += (n - zeroCnt) * 2 ** k

        return score 
