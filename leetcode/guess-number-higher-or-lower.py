# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l , h = 1, n
        while l <= h:
            midd = (l + h) //2 
            if guess(midd) == 0:
                return midd
            if guess(midd) == -1:
                h = midd - 1
            else:
                l = midd + 1
        return l