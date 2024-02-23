class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n,ans =len(costs),  0
        costs.sort(key = lambda x : (x[0] - x[1]))
        for i in range(n):
            if i >= n//2:
                ans += costs[i][1]
            else:
                ans += costs[i][0]
        return ans


        
        