class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        #  x + x + 1 + x + 2 == num
        if (num - 3) % 3 == 0:
            x = int((num - 3 ) / 3)
            return [x, x + 1, x + 2]
        return []
        