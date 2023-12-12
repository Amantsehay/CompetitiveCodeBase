class Solution {
    public boolean isHappy(int n) {
        // so the brute force approach 
        // if there is cycle not 
        Set<Integer> set = new HashSet<>();
        while (set.add(n)){
            int rst = 0;
            while (n > 0){
                rst += (n % 10) * (n % 10);
                n /= 10;
            }
            n = rst;
            if (rst == 1) return true;
        }
        return false;
    }
}