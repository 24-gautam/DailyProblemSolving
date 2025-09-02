public class Solution {

    public bool Compare(int[] p , int[] q) {
        return p[0] == q[0] ? p[1] < q[1] : p[0] > q[0] ;
    }

    public int NumberOfPairs(int[][] points) {

        Array.Sort(points, (p, q) => Compare(p, q) ? -1 : 1); 
        
        int n = points.Length , res = 0 ;

        for(int i = 0 ; i < n - 1 ; i++) {
            int y = int.MaxValue , yi = points[i][1] ; 

            for(int j = i + 1 ; j < n ; j++) {
                int yj = points[j][1] ; 

                if(yj >= yi && y > yj) {
                    res++ ; 
                    y = yj ;
                }
            }
        }

        return res ;
    }
}