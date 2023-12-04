class Solution {
    public String mergeAlternately(String word1, String word2) {
        int i = 0, j = 0, n = word1.length(), m = word2.length();
        StringBuilder ans = new StringBuilder();
        while (i < n || j < m){
            if (i < n && j < m){
                ans.append(word1.charAt(i));
                ans.append(word2.charAt(j));
            }
            else if (i < n){
                ans.append(word1.charAt(i));
            }
            else if (j < m){
                ans.append(word2.charAt(j));
            }
            i++; j++;
        }
        return ans.toString();
    }
}