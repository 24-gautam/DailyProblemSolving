class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        var map = new HashMap<Integer , Integer>() ;
        int i = 0 , j = 0 , max = 1 ;

        while(i < nums.length) {
            map.put(nums[i] , map.getOrDefault(nums[i] , 0) + 1) ; 
            if(map.get(nums[i]) > k) {
                while(map.get(nums[i]) > k) map.put(nums[j] , map.get(nums[j++]) - 1) ;  
            }
            max = Math.max(max , ++i - j) ;
        }

        return max ;
    }

}