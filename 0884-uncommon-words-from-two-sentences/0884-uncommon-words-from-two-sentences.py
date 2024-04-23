class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        map1 , map2 = Counter(s1.split()) , Counter(s2.split()) 
        
        for key in map1 : 
            if map1[key] == 1 and key not in map2 : res.append(key) 
        
        for key in map2 : 
            if map2[key] == 1 and key not in map1 : res.append(key) 

        return res 