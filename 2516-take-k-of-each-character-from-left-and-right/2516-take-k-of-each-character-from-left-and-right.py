class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0 : return 0 
        
        a , b , c = [] , [] , [] 
        cnt_a , cnt_b , cnt_c , res = 0 , 0 , 0 , 1e9

        for i , j in enumerate(s) : 
            if j == 'a' and len(a) < k : a.append(i)
            if j == 'b' and len(b) < k : b.append(i)
            if j == 'c' and len(c) < k : c.append(i) 

        if len(a) + len(b) + len(c) != 3 * k : return -1 

        # print(a , b, c)

        for i in range(len(s) - 1 , -1 , -1) : 
            j = 0 

            if s[i] == 'a' : cnt_a += 1 
            if s[i] == 'b' : cnt_b += 1 
            if s[i] == 'c' : cnt_c += 1 

            if cnt_a >= k and cnt_b >= k and cnt_c >= k : 
                res = min(len(s) - i , res) 
                # print(res , '|')
                break 

            if cnt_a < k : j = max(j , a[k-cnt_a-1])
            if cnt_b < k : j = max(j , b[k-cnt_b-1]) 
            if cnt_c < k : j = max(j , c[k-cnt_c-1]) 

            res = min(res , len(s) - i + j + 1) 
            # print(res)

        return res
