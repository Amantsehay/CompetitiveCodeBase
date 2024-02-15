class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        # so for each open parenthesis find a closing one 
        left, right = 0, 0
        for bracket in s:
            if bracket == '(':
                left += 1
            elif left > 0:
                left -= 1
            else:
                right += 1
        return left + right