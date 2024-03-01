class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        


        def solve(s):
            if not s:
                return ""
  
            string_set = set(s)
            for i in range(len(s)):
                curr_string = s[i]
                if curr_string.upper() in string_set and curr_string.lower() in string_set:
                    continue
                
                sub1 = self.longestNiceSubstring(s[i + 1:])
                sub2 = self.longestNiceSubstring(s[:i])
                return sub1 if len(sub1) > len(sub2) else sub2
            return s
        return solve(s)