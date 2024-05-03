class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = [[0 for j in range(len(image[0]))]for i in range(len(image))]

        return self.bfs(image , sr , sc , color , visit , image[sr][sc]) 

    def bfs(self, image , i , j , color , visit , n) : 
        if i >= 0 and j >= 0 and i < len(image) and j < len(image[0]) and not visit[i][j] and image[i][j] == n : 
            image[i][j] = color 
            visit[i][j] = 1 
            self.bfs(image , i + 1 , j , color , visit , n) 
            self.bfs(image , i , j + 1 , color , visit , n) 
            self.bfs(image , i - 1 , j , color , visit , n)
            self.bfs(image , i , j - 1 , color , visit , n) 

        return image