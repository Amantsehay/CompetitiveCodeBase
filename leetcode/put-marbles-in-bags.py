class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        arr = [0] * (n - 1)
        for i in range(1, n):
            arr[i -1] = weights[i] + weights[i - 1]
        print(arr)
        arr.sort()
        maxx = 0
        minn = 0
        for i in range(k-1):
            maxx += arr[n - 2 -i]
            minn += arr[i]
        return maxx - minn


        
        