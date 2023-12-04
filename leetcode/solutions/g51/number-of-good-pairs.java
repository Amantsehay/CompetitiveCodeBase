class Solution {
    public int numIdenticalPairs(int[] nums) {
        int n = nums.length;
        int ans = 0;
        int [] map = new int [101];
        for (int i = 0; i < n; i++){
            map[nums[i]]++;  
        }
        for (int i = 0; i < 101; i++){
            ans += (map[i] * (map[i] - 1))/2;
        }
        return ans;  
    }
}