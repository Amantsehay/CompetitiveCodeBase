class Solution:
    def smallestNumber(self, num: int) -> int:
        #if positve 
        #sort it and put the 0 in the middle 
        n = len(str(num))
        val = num
        num = [i for i in str(num) if i != "0" and i != "-"]
        print(num)
        if val == 0:
            return 0
        if val > 0:
            num.sort()
            rslt = num[0] + "0" * (n - len(num))
            if len(num) > 1:
                rslt += "".join(num[1:])
            return int(rslt)
            

        else:
            num.sort(reverse = True)
            return -1 * int("".join(num)  + "0" * (n - len(num) - 1))
