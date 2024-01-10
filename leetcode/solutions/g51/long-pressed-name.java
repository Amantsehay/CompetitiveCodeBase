class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int n = name.length(), m = typed.length();
        int l = 0, r = 0;
        if (m < n) return false;
        while (l < m){
            if (r < n && name.charAt(r) == typed.charAt(l)){
                l++; r++;
            }
            else {
                // if they are not equal 
                if (l ==0 || r == 0) return false;
                if (typed.charAt(l) != typed.charAt(l - 1)) return false;
                l++;
            }
        }
        return r == n;
    }
}