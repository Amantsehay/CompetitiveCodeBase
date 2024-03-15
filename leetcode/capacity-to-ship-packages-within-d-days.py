class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(weight):
            curr, ans = 0, 1
            for w in weights:
                curr += w
                if curr > weight:
                    ans += 1
                    curr = w
                if ans > days:
                    return False
            return ans <= days
        start, end = max(weights), sum(weights)
        while start <= end:
            mid = (start + end) //2 
            if isValid(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start

    

        