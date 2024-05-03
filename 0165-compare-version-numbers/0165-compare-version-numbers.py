class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 , s2 = version1.split('.') , version2.split('.') 
        m , n , i , j = len(s1) , len(s2) , 0 , 0

        while i < m or j < n : 
            if i >= m and int(s2[j]) > 0 : return -1 
            if j >= n and int(s1[i]) > 0 : return 1 
            if i < m and j < n and int(s1[i]) < int(s2[j]) : return -1 
            if i < m and j < n and int(s1[i]) > int(s2[j]) : return 1
            i += 1
            j += 1
        
        return 0