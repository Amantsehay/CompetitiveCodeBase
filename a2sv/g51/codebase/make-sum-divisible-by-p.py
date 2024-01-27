class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n, t, ps, hm = len(nums), sum(nums) % p, 0, {0: -1}
        ans = n
        
        if not t:
            return 0
        
        for i, num in enumerate(nums):
            ps += num
            k = (ps % p - t) % p
            if k in hm:
                ans = min(ans, i - hm[k])
            hm[ps % p] = i
        
        return ans if ans < n else -1
