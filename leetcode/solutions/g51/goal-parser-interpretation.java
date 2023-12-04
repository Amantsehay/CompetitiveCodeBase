class Solution {
    public String interpret(String command) {
        int n = command.length();
        String ans = "";
        for (int i = 0; i < n; i++){
            if (command.charAt(i) == 'G') ans += 'G';
            if (command.charAt(i)== '(' ){
                if (command.charAt(i + 1) == ')' ) ans += 'o';
                else ans += "al";
            }
        } 
        return ans;
    }
}