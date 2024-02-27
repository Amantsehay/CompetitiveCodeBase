class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(idx, curr):
            if idx >= len(nums):
                ans.append(curr[:])
                return 

            curr.append(nums[idx])
            print(curr)
            backtrack(idx + 1, curr)


            curr.pop()
            print(curr)
            backtrack(idx + 1, curr)
            
        
        curr = []
        backtrack(0, curr)
        return ans