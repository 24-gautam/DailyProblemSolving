class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0 

        for s in logs : 
            if s[:2] == '..' and cnt > 0 : cnt -= 1 
            elif '..' != s[:2] != './' : 
                cnt += 1 

        return cnt 