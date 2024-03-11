class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        counter = Counter(letters)
        ls = list(counter.keys())
        for cr in ls:
            if cr > target:
                return cr
        return letters[0]