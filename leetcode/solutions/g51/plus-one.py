class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_ = 0
        pow = 0
        for i in range(len(digits) - 1, - 1, -1):
            sum_ += digits[i]*10**pow
            pow+=1
        
        ans = res = [int(x) for x in str(sum_ + 1)]
        return ans
      

        