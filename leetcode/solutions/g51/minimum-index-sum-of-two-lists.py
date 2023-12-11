class Solution:
    def findRestaurant(self, A, B):
        index_map = {u: i for i, u in enumerate(A)}
        best, ans = 1e9, []
        for j, v in enumerate(B):
            i = index_map.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans
        
        