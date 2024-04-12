class Solution:
    def secondHighest(self, s: str) -> int:
        highest , secondHighest = -1 , -1 

        for c in s : 
            if c.isdigit() and int(c) > highest : highest , secondHighest = int(c) , highest 
            elif c.isdigit() and highest > int(c) > secondHighest : secondHighest = int(c) 
        
        return secondHighest 