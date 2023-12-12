class Solution {
    public String reverseWords(String s) {
        s = s.strip();
        int n = s.length();
        int end = n - 1;
        int start = n - 1;
        StringBuilder ans = new StringBuilder();

        while (end >= 0) {
            if (s.charAt(end) != ' ') {
                end--;
            }
            if (end == -1 || s.charAt(end) == ' ') {
                ans.append(s, end + 1, start + 1).append(" ");
                if (end == -1) break;
                while (s.charAt(end) == ' ') {
                    end--;
                }
                start = end;
            }
        }

        return ans.toString().strip();
    }
}
