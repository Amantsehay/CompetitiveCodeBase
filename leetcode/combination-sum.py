class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []        
        curr = []
        mp = set()
        def backtrack(target, idx):

            if target <= 0 or idx >= len(candidates):
                if target == 0:
                    ans.append(curr[:])
                return 

         
            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                target -= candidates[i]
                backtrack(target, i)
                curr.pop()
                target += candidates[i]
        

        backtrack(target, 0)
        return ans