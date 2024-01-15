class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        ans = 0
        prefix = 0
        count = { 0: 1}
        for r in range(n):
            prefix += nums[r] % 2
            need = prefix - k
            if need in count:
                ans += count[need]
            count[prefix] = count.get(prefix, 0) + 1
        return ans



