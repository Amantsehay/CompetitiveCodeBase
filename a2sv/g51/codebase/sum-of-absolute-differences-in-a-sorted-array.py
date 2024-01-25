class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum, right_sum, res, n = 0, sum(nums), [], len(nums)
        for i, num in enumerate(nums):
            res.append(i * num - left_sum + right_sum - (n - i) * num)
            left_sum += num
            right_sum -= num
        return res

