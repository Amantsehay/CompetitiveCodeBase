class Solution {
    
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int max = Integer.MIN_VALUE;
        int ans = 0;
        for (int i = 0; i < n; i++){
            ans = Math.max(nums[i], ans + nums[i]);
            max = Math.max(ans, max);

        }
        return max;
        
    }
}