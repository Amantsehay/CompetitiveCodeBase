class Solution {
    public int fun(char c){
        if(c=='a' || c=='e' || c=='i' || c=='u' || c=='o')
            return 1;
        return 0;
    } 
    public int maxVowels(String s, int k) {
        int n = s.length();
        int ans = 0;
        int max = 0;
        for(int i=0; i<k; i++)
            ans+=fun(s.charAt(i));
        max = ans;
        for(int i=1; i<=n-k; i++){
            ans = ans - fun(s.charAt(i-1)) + fun(s.charAt(i+k-1));
            max = Math.max(max,ans);
        }
        return max;
    }
}