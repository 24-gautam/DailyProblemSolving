class Solution:
    def minSteps(self, n: int) -> int:
        factors = []
        
        # Handle the smallest prime factor, 2
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        # Check for odd factors from 3 to sqrt(n)
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        
        # If n is still greater than 2, then n is a prime number
        if n > 2:
            factors.append(n)
        
        return sum(factors)  