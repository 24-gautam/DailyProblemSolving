class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dir = [[0,1] , [1,0] , [0,-1] , [-1,0]]
        currDir , currLoc = 0 , [0 , 0]
        s , res = set(tuple(l) for l in obstacles) , -2 ** 32

        for c in commands : 
            if c == -1 : currDir = (currDir + 1) % 4 
            if c == -2 : currDir = (currDir - 1) % 4 
            else : 
                i = 0 
                t = (currLoc[0] , currLoc[1])
                while i < c : 
                    temp = (currLoc[0] + (i + 1) * dir[currDir][0] , currLoc[1] + (i + 1) * dir[currDir][1]) 
                    print(temp , end = ' ')
                    if temp in s :
                        break 
                    i += 1 
                    t = temp 
                    res = max(res , t[0] ** 2 + t[1] ** 2)
                currLoc = [t[0] , t[1]] 

        return res