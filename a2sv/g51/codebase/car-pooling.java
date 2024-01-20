class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int n = trips.length;
        // max time completixy of 1000
        int max = 0;
        for (int i = 0; i < n; i++) max = Math.max(max, trips[i][2]);
        int [] dp = new int [max + 1];
        for (int i = 0; i < n; i++){
            int [] ls = trips[i];
            int p = ls[0], start = ls[1], end = ls[2];
            dp[start] += p; dp[end] -= p;
        }
        for (int i = 1; i <= max; i++){
            dp[i] += dp[i - 1];
            if (dp[i] > capacity) return false;
        }
        return true && dp[0] < capacity;

        
    }
}