class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
         costs.sort()
         tot = 0
         count = 0
         for num in costs:
             tot +=num
             if tot <= coins:
                 count +=1

         return count
