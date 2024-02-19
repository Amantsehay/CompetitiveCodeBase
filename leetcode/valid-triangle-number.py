class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n -1, 0, -1):
            start = 0
            end = i - 1
            curr = nums[i]
            while start < end:
                if nums[start] + nums[end] > curr:
                    ans += end - start
                    end -= 1
                else:
                    start += 1
        return ans
