class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = [True] * len(candies)
        for i in range(len(candies)):
            ans[i] = extraCandies + candies[i] >= max_candies
                
        return ans