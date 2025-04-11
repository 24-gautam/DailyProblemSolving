public class Solution {
    public int CountSymmetricIntegers(int low, int high) {
        var list = Enumerable.Range(low, high - low + 1).ToList(); 

        var res = list.Count(x => x.ToString().Length % 2 == 0 && 
                             x.ToString().Take(x.ToString().Length / 2).Sum(c => c - '0') == 
                             x.ToString().Skip(x.ToString().Length / 2).Sum(c => c - '0')
                            );
        return res;
    }
}