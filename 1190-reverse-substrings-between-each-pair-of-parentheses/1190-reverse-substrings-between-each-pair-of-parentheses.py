class Solution:
    def reverseParentheses(self, s: str) -> str:
        i , stk , idx = 0 , [] , -1

        while i < len(s) : 
            if s[i] == '(' : 
                stk.append(idx) 
                idx = i

            elif s[i] == ')' : 
                stk.append(i)
                stk = stk[:idx] + stk[idx:][::-1] 
                idx = stk[-1]
            else : 
                stk.append(s[i])
            i += 1
            
        s = '' 

        for c in stk : 
            if type(c) != int : 
                s += c

        return s 
        

