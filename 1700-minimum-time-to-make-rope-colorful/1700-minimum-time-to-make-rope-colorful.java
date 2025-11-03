class Solution {
    public int minCost(String colors, int[] neededTime) {
        int min = 0 ;
        
        for(int i = 0 ; i < colors.length() ; i++) {
            int j = i + 1 , sum = neededTime[i] , currMax = neededTime[i] ;
            while(j < colors.length() && colors.charAt(j) == colors.charAt(i)) {
                sum += neededTime[j] ;
                currMax = Math.max(neededTime[j++] , currMax) ;
            }
            i = j - 1 ;
            min += i == j ? 0 : (sum - currMax) ;
        }

        return min ;
    }
}