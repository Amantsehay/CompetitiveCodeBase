class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0

        n = len(firstList)
        m = len(secondList)
        ans = []

        while i < n and j < m:
            end = min(firstList[i][1], secondList[j][1])
            start = max(firstList[i][0], secondList[j][0])
            if end >= start:
                ans.append([start, end])
            if firstList[i][1] >= secondList[j][1]:
                j += 1
            else:
                i += 1
        return ans


        