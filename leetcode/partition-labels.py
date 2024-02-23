class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # with a dictitionary store the last occerence of the chars 
        n = len(s)
        lastIndex = [0] * 26
        end = 0
        prev = 0
        ans = []
        for i in range(n):
            lastIndex[ord(s[i]) - ord('a')] = i
        for i in range(n):
            end = max(end, lastIndex[ord(s[i]) - ord('a')])
            if end == i:
                ans.append(end + 1 - prev)
                prev = i + 1
        return ans


        