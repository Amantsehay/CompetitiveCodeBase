class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n, target, prefix, count = len(nums), sum(nums) % p, 0, {0: -1}
        ans = n
        
        if not target:
            return 0
        
        for i, num in enumerate(nums):
            prefix += num
            k = (prefix % p - target) % p
            if k in count:
                ans = min(ans, i - count[k])
            count[prefix % p] = i
        
        return ans if ans < n else -1
