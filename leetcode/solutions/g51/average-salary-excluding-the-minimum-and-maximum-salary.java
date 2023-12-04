class Solution {
    public double average(int[] salary) {
        int max  = 0, min = Integer.MAX_VALUE;
        int sum = 0;
        int n = salary.length;
        for (int num : salary){
            max = Math.max(max, num);
            min = Math.min(num, min);
            sum += num;
        }
        return (double) (sum - max - min) / (n - 2);
        
    }
}