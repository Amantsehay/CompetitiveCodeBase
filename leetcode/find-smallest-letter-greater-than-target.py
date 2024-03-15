class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        low, high = 0, len(letters) - 1
        while low < high:
            midd = (low + high) //2 
            if letters[midd] > target:
                high = midd
            else:
                low = midd + 1
        print(low)
        return letters[low] if letters[low] > target else letters[0]


        