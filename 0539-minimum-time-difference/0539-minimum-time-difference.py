class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort() 
        mn , n = float('inf') , len(timePoints)

        for i in range(1 , n + 1) : 
            currMin = int(timePoints[i%n][3:]) 
            prevMin = int(timePoints[i-1][3:])
            currHr = int(timePoints[i%n][:2]) 
            prevHr = int(timePoints[i-1][:2]) 

            if i == n : 
                currMin , prevMin , currHr , prevHr = prevMin , currMin , prevHr , currHr

            minutes = currMin - prevMin if currMin >= prevMin else currMin + 60 - prevMin 
            hours = currHr - prevHr - 1 if currMin < prevMin else currHr - prevHr 

            mn = min(mn , minutes + hours * 60 , 24 * 60 - minutes - hours * 60) 
       
        return mn