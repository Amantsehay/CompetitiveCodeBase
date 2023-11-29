class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # just take on tring
        common = strs[0]
        for i in range(1, len(strs)):
            curr = strs[i]
            i = 0
            j = 0
            cm = ""
            while ( i < len(curr) and j < len(common)):
                if (curr[i] == common[j]):
                    cm += curr[i]
                else:
                    break
                i += 1
                j += 1
            common = cm
        return common



        