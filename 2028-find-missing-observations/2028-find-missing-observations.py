class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        mSum = sum(rolls)
        totalSum = (len(rolls) + n) * mean  
        if totalSum < mSum + n : return []
        reqSum = totalSum - mSum 
        res = [] 

        curr = 1 

        while n : 
            while curr + 6 * (n - 1) < reqSum : curr += 1
            if curr > 6 : return [] 
            res.append(curr) 
            reqSum -= curr 
            n -= 1 

        print(totalSum)
        return res 