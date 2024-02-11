
from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        check=defaultdict(list)
        n = len(nums)
        for i in range(n):
            check[nums[i]].append(i)
        ans =  [0] * n
    # for each indices then find the right and left sum

        for key in check:
            prefix = 0
            ls = check[key]
            tot = sum(ls)
            for i, ind in enumerate(ls):
                curr = ind * i - prefix + (tot - prefix ) - ind * (len(ls) - i)
                prefix += ind
                ans[ind] = curr
        return ans
