class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph , visited = [[] for i in range(n)] , [0] * n 
        
        for edge in edges : 
            graph[edge[0]].append(edge[1]) 
            graph[edge[1]].append(edge[0]) 

        self.dfs(source , destination , graph , visited)  
        return visited[destination]

    def dfs(self , src , dst , graph , visited) : 
        visit = 0 
        if visited[dst] : return 1
        visited[src] = 1 

        for node in graph[src] : 
            if not visited[node] : 
                visit = self.dfs(node , dst , graph , visited) 
        
        return visit 