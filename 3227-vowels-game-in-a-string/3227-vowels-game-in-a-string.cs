public class Solution {
    public bool DoesAliceWin(string s) {
        int countVowel = s.Count(c => "aeiou".Contains(c)) ; 

        return countVowel == 0 ? false : true ; 

    }
}