class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # window length of 3
        ans = 0
        rslt = -1
        for i in range(len(num)):
            if i >= 2:
                ans = int(num[i - 2: i + 1])
                if ans  % 111 == 0:
                    rslt = max(rslt, ans)
                
        return str(rslt) if rslt >  0 else ( "000"  if rslt  == 0 else "")







        