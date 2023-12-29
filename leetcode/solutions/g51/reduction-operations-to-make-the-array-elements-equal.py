class Solution:
    def reductionOperations(self, num: List[int]) -> int:
        # count sort them 
        num.sort(reverse = True)
        count = 0
        ans = 0
        for i in range(len(num) - 1):
            count += 1
            if num[i] != num[i + 1]:
                ans += count
        return ans
            

        