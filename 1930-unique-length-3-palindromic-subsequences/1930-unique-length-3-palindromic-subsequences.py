class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic , count = {} , 0

        for i in range(len(s)) :
            if dic.get(s[i]) == None :
                dic[s[i]] = [i , i] ;
            else :
                dic[s[i]] = [dic[s[i]][0] , i]
        
        print(dic)

        for key in dic :
            hashSet = set()
            i , j = dic[key]

            for k in range(i + 1 , j) :
                hashSet.add(s[k])
            
            count += len(hashSet)
        
        return count 