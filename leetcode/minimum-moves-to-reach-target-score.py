class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        if target <= 1:
            return 0

        # Start at the back and move to the one 
        ans = 0

        while target > 1:
            if maxDoubles > 0:
                if target % 2:
                    ans += 1
                target //= 2
                maxDoubles -= 1
                ans += 1
            else:
                ans += target - 1
                break
        return ans


        
        

        
        