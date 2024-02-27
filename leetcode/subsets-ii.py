class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        curr = []
        nums.sort()
        ans = []
        def backtrack(idx):
            if idx > len(nums):
                return 

            ans.append(curr[:])
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()
            return 
        backtrack(0)
        return ans


        