class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1]) 
        minArrow , i = 0 , 0 

        while i < len(points) : 
            j = i + 1 
            while j < len(points) and points[j][0] <= points[i][1] <= points[j][1] : 
                j += 1 
            i , minArrow = j , minArrow + 1 

        return minArrow