class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int zeros = 0, i = 0, ans = 0;
        for (int j = 0; j < n; j++) {
            if (nums[j] == 0) {
                zeros++;
            }
            while (zeros > k) {
                if (nums[i] == 0) {
                    zeros--;
                }
                i++;
            }

            ans = Math.max(ans, j - i + 1);
        }

        return ans;
    }
}
