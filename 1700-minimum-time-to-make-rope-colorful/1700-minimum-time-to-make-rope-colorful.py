class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res , curr , mx = 0 , 0 , 0 

        for i in range(len(colors)) : 
            if i > 0 and colors[i] != colors[i-1] : 
                res += curr - mx 
                mx = curr = neededTime[i]
            else : 
                mx = max(mx, neededTime[i])
                curr += neededTime[i] 

        return res + ((curr - mx) if i > 0 and colors[i] == colors[i-1] else 0)
