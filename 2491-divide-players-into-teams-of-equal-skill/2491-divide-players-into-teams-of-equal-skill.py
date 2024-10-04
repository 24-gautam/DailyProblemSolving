class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort() 

        i , j , res , k = 0 , len(skill) - 1 , 0 , skill[0] + skill[-1] 

        while i < j : 
            if skill[i] + skill[j] == k : res += skill[i] * skill[j]
            else : return -1 
            i += 1 
            j -= 1

        return res