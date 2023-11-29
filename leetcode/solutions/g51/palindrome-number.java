class Solution {
    public boolean isPalindrome(int x) {
        String theNum="" +x;
        for (int i=0; i<theNum.length()/2; i++){
            if (theNum.charAt(i)!=theNum.charAt(theNum.length()-i-1))
            return false;
        }
        return true;

    }

    }
