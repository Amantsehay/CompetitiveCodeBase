class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    

        count = Counter(arr)
        n = len(arr)
        forUse = 0
        currMax = n
        for i in range(n):
            if arr[i] > n:
                forUse += 1
        while n > 1:
            if n in count:
                forUse += count[n] -1
            else:
                if forUse > 0:
                    forUse -= 1
                else:
                    currMax -= 1
            n -= 1
        return currMax

        
   

                                                                            