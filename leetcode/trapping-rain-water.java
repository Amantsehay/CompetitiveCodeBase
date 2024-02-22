class Solution {
    public int trap(int[] height) {
        // this got be done with the brain fuck 

        int n = height.length;
        int [] rightMax = new int [n];
        int [] leftMax = new int [n];
        int sumResult = 0;
        for (int i = 0; i < n; i++){
            rightMax [i] = i == 0? height[i]: Math.max(rightMax[i - 1], height[i]);
        }
    for (int j = n - 1; j >= 0; j--){
            leftMax[j] = j == n - 1? height [j]: Math.max(leftMax[j + 1], height[j]);

        }
        for (int k = 0; k < n; k++)
        sumResult += Math.min(leftMax[k], rightMax[k]) - height[k];
        return sumResult;

        
    }
}