class Solution {
    public int longestSubarray(int[] nums) {
        int zeros = 0, n = nums.length, l = 0, ans = 0;

        for (int i = 0; i < n ; i++){
            if (nums[i] == 0) zeros++;
            while (l < n && zeros > 1){
                if (nums[l++] == 0) zeros--;
            }
            
            ans = Math.max(i -l, ans);
        }
        return ans;
        
    }
}