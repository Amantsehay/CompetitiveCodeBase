class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int m = s1.length(), n = s2.length(), l = 0, r = 0;
        int ans = Integer.MAX_VALUE, cnt = 0;
        int [] map = new int [128];
        for (char c : s1.toCharArray()) map[c]++;
        while (r < n){
            if (--map[s2.charAt(r++)] >= 0) cnt++;
            while (cnt == m) {
                ans = Math.min(ans, r - l);
                if (ans == m) return true;
                if (++map[s2.charAt(l++)] > 0) cnt--;
            }
        }
return ans == m;   
    }
}