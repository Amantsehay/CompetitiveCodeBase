import java.util.*;
class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> map = new HashMap<>();
        int index = 0, n = words.length;
        for (char c : order.toCharArray()){
            map.put(c, index++);
        }
        for (int i = 0; i < n - 1; i++){
            if (!compare(words[i], words[i  + 1], map))  return false;
        }
        return true;
    }

    private boolean compare(String w1, String w2, Map<Character, Integer> map){
        int n = w1.length(), m = w2.length();
        int i = 0, j = 0;
        while (i < n && j < m ){
            if (map.get(w1.charAt(i)) <  map.get(w2.charAt(j))){
                return true;
            }
            if (map.get(w1.charAt(i)) >  map.get(w2.charAt(j))){
                return false;
            }
            i++; j++;
        }
        return i == n;

    }
}