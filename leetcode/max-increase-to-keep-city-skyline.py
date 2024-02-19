class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        arr1=[max(i) for i in grid]
        arr2=[]
        l=len(grid)
        for i in range(l):
            c=max([j[i] for j in grid])
            arr2.append(c)
        ans=0
        for i in range(l):
            for j in range(l):
                ans+=min(arr1[i],arr2[j])-grid[i][j]
        return ans