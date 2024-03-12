//BRUTE FORCE - 1(HASHMAP + FREQ ARRAY)

class Solution {
    public String customSortString(String order, String s) {
        Map<Character, Integer> map = new HashMap<>();
        String ans = "";
        int[] freq = new int[26];
        
        //MAPPING FREQ FOR STRING --> S
        for(char c: s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0)+1);
        }
        
        //ALL UNIQUE COMMON OCCURENCES OF ORDER & S ARE STORED IN ORDER IN ANS
        for(char c: order.toCharArray()){
            if(map.containsKey(c)){
                int x = map.get(c);
                while(x > 0){
                    ans += c;
                    x--;
                }
                map.remove(c);
            }
        }
        
        if(!map.isEmpty()){
            //MAPPING LEFTOVER FREQUENCY
            for(char c: map.keySet()){
                freq[c - 'a'] = map.get(c);
            }
        }else{
            return ans;
        }
        for(int i=0 ; i<26 ; i++){
            while(freq[i] > 0){
                ans += (char)(i + 'a');
                freq[i]--;
            }
        }
        
        return ans;
    }
}