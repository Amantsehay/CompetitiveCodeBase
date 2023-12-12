
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer , Integer> theHash= new HashMap<>();
        int [] pair=new int [2];
        for (int i=0 ; i<nums.length; ++i){
            if (theHash.containsKey(target- nums[i])){
                pair[0]=theHash.get(target-nums[i]);
                pair[1]=i;
                break;
            }
            theHash.put(nums[i], i);
        }
        return pair;
   
    }
}