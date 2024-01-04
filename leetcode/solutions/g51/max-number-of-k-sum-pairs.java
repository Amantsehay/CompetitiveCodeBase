class Solution {
    public int maxOperations(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        for (int i = 0; i < nums.length; i++){
            int need = k - nums[i];
            if (map.containsKey(need) && map.get(need) > 0){
                ans++;
                map.put(need, map.get(need) - 1);
            }
            else 
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        return ans; 
    }
}