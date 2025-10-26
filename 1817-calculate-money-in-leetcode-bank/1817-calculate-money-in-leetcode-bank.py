class Solution:
    def totalMoney(self, n: int) -> int:
        sum = 0 

        for i in range(1 , n + 1) :
            sum += (6 + i // 7) if i % 7 == 0 else i // 7 + i % 7
        
        return sum 