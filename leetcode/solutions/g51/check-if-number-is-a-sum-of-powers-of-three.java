class Solution {
    public boolean checkPowersOfThree(int n) {
        if (n == 1) return true;
        if (n <= 0 || n % 3 == 2) return false;
        if (n % 3 == 0) return checkPowersOfThree(n / 3);
        else return checkPowersOfThree(n - 1);
    }
}

/**
91 / 3 
27
9
3
1
3 * 1 + 3 * 1


91 = to base of 3
ternary three 

5
4
return false



21

2
0

return false


17


 */