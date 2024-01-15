class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int i= 0, ans = n + 1, totSum = 0;
        for (int j = 0; j < n; j++){
            totSum += nums[j];

            while (totSum >= target){
                totSum -= nums[i];
                ans = Math.min(ans, j - i + 1);
                i++;
            }
        }
        return ans == n + 1 ? 0 : ans;


        
    }
}