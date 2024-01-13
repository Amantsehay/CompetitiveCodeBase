class Solution {
    public int characterReplacement(String s, int k) {
        // this is to keep track of the max length 
        int n = s.length(), ans = 0, l = 0;
        int [] map = new int [26];
        int maxFreq = 0;
        for (int i = 0; i < n; i++){
            char c = s.charAt(i);
            map[c - 'A']++;
            maxFreq = Math.max(maxFreq, map[c - 'A']);
            while (i - l  + 1  - maxFreq > k){
                map[s.charAt(l++) - 'A']--;
            }
            ans  = Math.max(ans, i - l + 1);
        }
        return ans; 
    }
}