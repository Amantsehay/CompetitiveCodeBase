class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # the maximum I can patch is the number itself
       
        tot = 0
        idx = 0
        curr = 1
        ans  = 0
        m = len(nums)
        while curr < n + 1:
            while idx < m and nums[idx] <= curr:
                tot += nums[idx]
                idx += 1
            if tot < curr:
                tot += curr
                ans += 1
                curr = tot
            curr += 1
        return ans
                
            


        

            
            # 


