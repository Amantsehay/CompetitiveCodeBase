from collections import Counter 

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter =  Counter(arr)
        for l in counter:
            if counter[l] > 0.25 * len(arr):
                return l
        return 0



        
        