class Solution {
    int rowMin(int [] nums) {
        int min = Integer.MAX_VALUE ; 
        for(int i : nums) min = Math.min(min , i) ; 
        return min ;
    }
    int colMax(int [][] nums , int col) {
        int max = Integer.MIN_VALUE ; 
        for(int i = 0 ; i < nums.length ; i++) max = Math.max(max , nums[i][col]) ; 
        return max ;
    }

    public List<Integer> luckyNumbers (int[][] matrix) {
        List<Integer> res = new ArrayList<>() ;
        Map<Integer , Integer> map = new HashMap<>() ;
        
        for(int i = 0 ; i < matrix[0].length ; i++) map.put(colMax(matrix , i) , i) ;
        for(int i = 0 ; i < matrix.length ; i++) {
            int num = rowMin(matrix[i]) ;
            if(map.containsKey(num)) res.add(num) ;
        }
        return res ;
    }
}