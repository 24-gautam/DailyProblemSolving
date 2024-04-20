class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        farmLand = []

        for i in range(len(land)) : 
            for j in range(len(land[0])) : 
                if land[i][j] == 1 : 
                    bottomRight = [i , j]
                    self.bfs(land , i , j , bottomRight) 
                    farmLand.append([i , j , bottomRight[0] , bottomRight[1]]) 
        
        return farmLand 

    def bfs(self , land , i , j , arr) : 
        if i == len(land) or j == len(land[0]) or not land[i][j] or land[i][j] == 2 : return 
        x = 1 if len(land) == i + 1 or not land[i+1][j] else 0 
        y = 1 if len(land[0]) == j + 1 or not land[i][j+1] else 0 
        land[i][j] = 2
        if x and y : 
            arr[0] , arr[1] = i , j

        self.bfs(land , i , j + 1 , arr)
        self.bfs(land , i + 1 , j , arr)