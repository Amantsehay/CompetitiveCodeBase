class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isValid(mass):
            curr = 0
            for p in piles:
                curr += math.ceil(p / mass)
                if curr > h:
                    return False
            return True

        low, high = 1, max(piles)

        while low <= high:
            midd = (low + high) // 2
            if isValid(midd):
                high = midd - 1
            else:
                low = midd + 1
        return low
        