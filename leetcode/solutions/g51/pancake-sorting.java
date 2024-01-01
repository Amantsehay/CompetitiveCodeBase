class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        List<Integer> ans = new ArrayList<>();
        
        int len = arr.length;
        for (int n = len - 1; n > 0; n--){
            for (int i = 1 ; i <= n; i++ ){
                if (arr[i] == n + 1){
                    reverse(arr, i);
                    ans.add(i + 1);
                    break;
                }

            }
            reverse(arr, n);
            ans.add(n + 1);
            
        }


        return ans;
        
    }

    private void reverse(int[] A, int k) {
        for (int i = 0, j = k; i < j; i++, j--) {
            int tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
        }
}}