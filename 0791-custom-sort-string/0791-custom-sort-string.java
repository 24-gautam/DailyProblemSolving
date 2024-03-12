//BRUTE FORCE - 1(HASHMAP + FREQ ARRAY)

class Solution {
    public String customSortString(String order, String s) {
        Map<Character, Integer> map = new HashMap<>();
        String ans = "";
        
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
        
        for(var key : map.keySet()) {
            int n = map.get(key) ; 
            while(n-- > 0) ans += key ;
        }
        
        
        return ans;
    }
}