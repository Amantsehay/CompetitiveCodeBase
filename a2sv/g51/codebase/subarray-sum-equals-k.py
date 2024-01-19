class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = 0

        count = {}
        count[0] = 1
        for i in range(len(nums)):
            prefix += nums[i]
            need = prefix - k
            if need in count:
                ans += count[need]
            count[prefix] = count.get(prefix, 0) + 1

        return ans
        