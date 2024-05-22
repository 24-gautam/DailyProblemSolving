class Solution {
    List<List<String>> res = new ArrayList<>() ;
    
    public boolean isPalindrome(String s , int low , int high) {
        while(low < high) if(s.charAt(low++) != s.charAt(high--)) return false ; 
        return true ;
    }
    public List<List<String>> partition(String s) {
        partitionSolve(new ArrayList<>() , 0 , s) ;
        return res ;
    }
    public void partitionSolve(List<String> list , int idx , String s) {
        if(idx == s.length()) {
            res.add(new ArrayList<>(list)) ;
            return ;
        }
        for(int i = idx ; i < s.length() ; i++) {
            if(isPalindrome(s , idx , i)) {
                list.add(s.substring(idx , i + 1)) ;
                partitionSolve(list , i + 1 , s) ;
                list.remove(list.size() - 1) ;
            }
        }
    }
}