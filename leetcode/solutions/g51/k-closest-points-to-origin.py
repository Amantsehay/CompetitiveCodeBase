import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heapq.heappush(heap, (self.d(p), p))
        ls = []
        for _ in range(k):
            ls.append(heapq.heappop(heap)[1])

        return ls
    def d(self, p):
        return (p[0]**2 + p[1]**2)**0.5