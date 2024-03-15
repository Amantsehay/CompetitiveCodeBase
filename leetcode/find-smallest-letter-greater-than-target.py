class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        i, j = 0, len(letters) - 1
        while i <= j:
            midd = (i + j) // 2 
            if letters[midd] > target:
                j = midd - 1
            else:
                i = midd + 1
        
        return letters[i] if i != len(letters) else letters[0]
        