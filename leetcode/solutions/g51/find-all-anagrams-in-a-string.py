class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1 = [0] * 26
        d2 = [0] * 26
        n = len(s)
        k = len(p)
        ans = []
        for st in p:
            d1[ord(st) -  ord('a')] += 1
       
        for i in range(n):
            d2[ord(s[i]) - ord('a')] += 1
            if i >= k - 1:
                if self.comp(d1, d2):
                    ans.append(i - k + 1)
                d2[ord(s[i - k + 1]) - ord('a')] -= 1
        return ans

    def comp(self, d1, d2):
        for i in range(26):
            if d1[i] != d2[i]:
                return False
        return True


        