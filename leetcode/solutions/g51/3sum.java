import java.util.Arrays;
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length; Arrays.sort(nums);
        List<List<Integer>> ans = new LinkedList<>();
        for (int i = 0 ; i < n - 2; i++){
            if (i == 0 || ( i > 0 && nums[i] != nums[i - 1])){
                int l = i + 1, r = n - 1, sum = - nums[i];
                while (l < r){
                    if (nums[l] + nums[r] == sum){
                        ans.add(Arrays.asList(nums[i], nums[l], nums[r]));
                        while (l < r && nums[l]== nums[l++ + 1]);
                        while (l < r && nums[r] == nums[r-- - 1]);
                    }
                    else if (nums[l] + nums[r] > sum) r--;
                    else l++;
                }
            }
        }
        return ans;
        
    }
}