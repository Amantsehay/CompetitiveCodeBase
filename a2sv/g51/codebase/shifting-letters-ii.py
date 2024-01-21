class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        dp = [0] * n
        m = len(shifts)
        for i in range(m):
            start, end, direction = shifts[i]
            print(start)

            if direction == 1:
                dp[start] += 1
                if end + 1 < n:
                    dp[end + 1] -= 1
            else:
                dp[start] -= 1
                if end + 1 < n:
                    dp[end + 1] += 1
        for i in range(1, n):
            dp[i] += dp[i - 1]

        ans = []
        for i in range(n):
            shift = dp[i] % 26
            shi =(ord(s[i]) - ord('a') + shift ) % 26
            ans.append(chr(ord('a') + shi ))

        return "".join(ans)






        