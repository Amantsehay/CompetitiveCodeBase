class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # this is an increasing stack problem

        stack = []
        minn = nums[0]
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            minn = min(minn, curr)
            while stack and stack[-1][0] <= curr:
                val = stack.pop()
            if stack and stack[-1][1] < curr:
                return True
            stack.append((curr, minn))
            
        return False

        