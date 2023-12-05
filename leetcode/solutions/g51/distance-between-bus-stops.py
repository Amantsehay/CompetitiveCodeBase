class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        tot = sum(distance)
        path_one = self.path_sum(distance, start, destination)
        return min(path_one, tot - path_one)
    def path_sum(self, distance, start, end):
        ans = 0
        i = min(start, end)
        j = max(start, end)
        while (i < j):
            ans += distance[i]
            i += 1
        return ans
        

        