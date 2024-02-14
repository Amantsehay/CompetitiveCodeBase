class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # shot the fastest that comes up 

        points.sort(key = lambda x : x[1])
        n = len(points)
        start = points[0][1]
        print(points)
        ans = 1
        for i in range(n):
            if points[i][0] > start:
                ans += 1
                start = points[i][1]
        return ans
        

        