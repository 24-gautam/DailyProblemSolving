class Solution {
    public int pivotInteger(int n) {
        int left = 0 , sum = (n * (n + 1)) / 2 , i = 1 ; 
        while(left < sum - left + i - 1) left += i++ ;

        return 2 * left  == sum + i - 1 ? i - 1 : - 1 ; 
    }
}