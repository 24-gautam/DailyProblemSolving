class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        s , curr , sum = set() , 0 , 0

        while len(s) != n - 1 : 
            i = 0 
            while i < k and len(s) != n - 1 : 
                curr = n if (curr + 1) % n == 0 else (curr + 1) % n 
                if curr not in s : i += 1 
            s.add(curr) 
            sum += curr
        
        return (n * (n + 1)) // 2 - sum