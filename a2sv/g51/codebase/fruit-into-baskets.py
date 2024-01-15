class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        d = {}
        count = 0
        ans = 0
        l = 0
        for r in range(n):
            fruit = fruits[r]
            d[fruit] = d.get(fruit, 0) + 1
            if d[fruit] == 1:
                count += 1
            while count > 2:
                if d[fruits[l]] == 1:
                    count -= 1
                d[fruits[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans




        