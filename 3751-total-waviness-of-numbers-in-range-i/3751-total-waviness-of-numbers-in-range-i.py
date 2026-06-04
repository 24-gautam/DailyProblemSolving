class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0 

        for i in range(num1, num2 + 1) : 
            n = str(i) 
            for i in range(1, len(n)) : 
                if i + 1 < len(n) :
                    if (n[i] > n[i-1] and n[i] > n[i+1]) or n[i-1] > n[i] < n[i+1] : res += 1

        return res