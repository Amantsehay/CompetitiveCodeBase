class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        the_set = set(nums)
        ind ={}
        for i, val in enumerate(nums):
            ind[val] = i
        for op in operations:
            i = ind[op[0]]
            nums[i] = op[1]
            ind[op[1]] =i

        return nums