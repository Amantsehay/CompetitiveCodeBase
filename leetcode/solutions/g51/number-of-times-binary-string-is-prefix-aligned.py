class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        oneCount = 0
        n = len(flips)
        binary_string =  [0] * n
        ans = 0
        for i in range(n):
            binary_string[flips[i] - 1] = 1
            if binary_string[i] == 1:
                oneCount += 1
            if (flips[i] - 1 < i):
                oneCount += 1
            if oneCount == i + 1:
                ans += 1
        return ans


        