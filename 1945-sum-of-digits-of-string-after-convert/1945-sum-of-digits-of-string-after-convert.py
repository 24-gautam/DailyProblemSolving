class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l = ''.join(list(str(ord(i) - 96) for i in s)) 
        l = sum(map(int , l))

        if k == 1 : return l

        while k > 1 : 
            l = sum(map(int , str(l))) 
            k -= 1 

        return l