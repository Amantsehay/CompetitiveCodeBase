class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = 0
        count = {}
        count[0] = 1
        for i in range(len(nums)):
            prefix += nums[i]
            need = prefix % k
            if need in count:
                ans += count[need]
            count[need] = count.get(need, 0) + 1

        return ans
        