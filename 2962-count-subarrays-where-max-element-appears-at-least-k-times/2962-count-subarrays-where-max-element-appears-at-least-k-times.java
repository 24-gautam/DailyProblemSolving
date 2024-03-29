class Solution {
    public long countSubarrays(int[] nums, int k) {
        int max = 0 , cnt = 0 , i = 0 , j = 0 ;
        long res = 0 ;
        for(int num : nums) max = Math.max(max , num) ; 

        while(i < nums.length) {
            if(nums[i] == max) cnt++ ; 
            if(cnt >= k) {
                 res += (nums.length - i) ; 
                //  System.out.print(res + " " + i) ; 
                 while(cnt >= k) {
                    if(nums[j] == max) {cnt-- ; j++ ; break ;} 
                    res += (nums.length - i) ; j++ ; 
                 }
                // System.out.println(" " + j + " " + res ) ; 
            }
            i++ ; 
        }

        return res ; 
    }
}