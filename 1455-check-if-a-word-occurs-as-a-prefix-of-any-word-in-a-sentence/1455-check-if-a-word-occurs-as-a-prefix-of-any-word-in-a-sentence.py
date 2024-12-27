class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        res , flag , j = 1 , 1 , 0

        for i in sentence : 
            if flag and j == len(searchWord) : return res 
            elif i == ' ' : j , flag , res = 0 , 1 , res + 1
            elif flag and i == searchWord[j] : j += 1
            else : flag = 0 
        
        return res if j == len(searchWord) else -1