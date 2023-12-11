class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length, l = 0, r = n - 1;;
        int [] ans = new int [n];
        Arrays.fill(ans, pivot);
       for (int i = 0; i < n; i++){
           if (nums[i] < pivot) ans[l++] = nums[i];
           if (nums[n - i - 1] > pivot) ans[r--] = nums[n - 1 - i];
       } return ans;   
    }
}