class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        left_one = 0
        ans = 0
        if s[0] == '1':
            left_one += 1
        right_one = s.count('1') - left_one 
        
        for i in range(1, n - 1):
            if s[i] == '0':
                ans += left_one * right_one
            elif s[i] == '1' :
                right_one -= 1
                ans +=(i - left_one ) * (n - i - 1 - right_one)
                left_one += 1
        return ans



                

        