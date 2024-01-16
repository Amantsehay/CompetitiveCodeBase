class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        ans = 0
        curr = capacity
        for i in range(len(plants)):
            if  curr >= plants[i]:
                ans += 1
                curr -= plants[i]
            else:
                ans += 2 * i + 1
                curr = capacity - plants[i]
        return ans
        