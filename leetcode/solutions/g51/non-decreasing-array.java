class Solution {
    public boolean checkPossibility(int[] nums) {
        int bcount = 0, fcount = 0, n = nums.length;
        int last = Integer.MAX_VALUE;
        int first = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++){
            if (fcount <= 1 && nums[i] < first){
                 first = nums[i - 1];
                 fcount++;
            }
            else first  = nums[i];  
            if (bcount <= 1 && nums[n - i  - 1] > last){
                last = nums[n - i];
                bcount++;
            }
            else last = nums[n - i - 1];       
        }
        return bcount <=  1 || fcount <= 1;
    }

}