class Solution {

    public int mapValue(int num , int[] map) {
        if(num == 0) return map[0] ;
        int res = 0 ; 
        int t = 1 ;
        while(num > 0) {
            res += map[num % 10] * t ;
            num /= 10 ; t *= 10 ;
        }
        return res ;
    }
    public int[] sortJumbled(int[] map , int[] nums) {
        int arr[][] = new int [nums.length][2] ;

        for(int i = 0 ; i < nums.length ; i++) {
            arr[i][0] = nums[i] ;
            arr[i][1] = mapValue(nums[i] , map) ;
        }
        Arrays.sort(arr , (x , y) -> x[1] - y[1]) ;

		for(int i=0; i<nums.length; i++)
				nums[i] = arr[i][0] ;
                
		return nums ;
    }
}