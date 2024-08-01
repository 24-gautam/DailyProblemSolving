class Solution {
    public int countSeniors(String[] details) {
        int c = 0 ; 
        for(var s : details) {
            int num = (s.charAt(11) - '0') * 10 + (s.charAt(12) - '0') ;
            if(num > 60) c += 1 ;  
        }
        
        return c ; 
    }
}