class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []

        def backtrack(idx, curr):
            if idx == len(digits):
                ans.append(curr)
                return

            currIdx = int(digits[idx])
            for j in range(len(mp[currIdx])):
                backtrack(idx + 1, curr + mp[currIdx][j])

        backtrack(0, "")
        return ans
