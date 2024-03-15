class Solution:
    def mySqrt(self, x: int) -> int:

        # try them out 
        low, high = 0, x
        while low <= high:
            midd = (low + high) //2 
            if midd ** 2 == x:
                return midd
            if midd ** 2 > x:
                high = midd - 1
            else:
                low = midd + 1
        return high 
        