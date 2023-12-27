class Solution {
    public void sortColors(int[] nums) {

        int n = nums.length;
        
        int l = 0, r = n - 1, c = 0;
        while (c <= r){
            if (nums[c] == 2){
                swap(nums, c, r--);
                
            }
            else if (nums[c] == 1){
                
                c++;
            }
            else {
                swap(nums, c, l);
                c++;
                l++;
                
            }

        }

        
    }
    private void swap(int [] nums, int c, int i){
        int temp = nums[c];
        nums[c] = nums[i];
        nums[i] = temp;
    }
}