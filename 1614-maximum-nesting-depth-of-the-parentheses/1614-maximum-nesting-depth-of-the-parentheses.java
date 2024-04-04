class Solution {
    public int maxDepth(String s) {
        int res = 0 , cnt = 0 ; 

        for(char c : s.toCharArray()) {
            if(c == '(') cnt += 1 ; 
            else if(c == ')') cnt -= 1 ; 
            
            res = Math.max(res , cnt) ; 
        }

        return res ; 
    }
}