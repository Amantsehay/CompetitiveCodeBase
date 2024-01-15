class Solution {
    public String minWindow(String s, String t) {
        int n = s.length(), m = t.length(), l = 0, r = 0;
        int ans = n + 1, count = 0;
        int [] map = new int [128];
        for (char c : t.toCharArray()) map[c]++;
        int start = 0;
        while (r < n){
            if (--map[s.charAt(r++)] >= 0)count++;
            while (count == m){
                if (ans > r - l){
                    ans = Math.min(ans, r - l);
                    start = l;
                }
                if (++map[s.charAt(l++)] > 0)
                    count--;
        }}
        return ans == n + 1? "" : s.substring(start, start + ans);  
    }
}