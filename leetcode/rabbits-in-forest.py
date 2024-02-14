class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        count = Counter(answers)
        ans = 0
        for key in count:
            curr = count[key]
            print(curr)
            ans += math.ceil(curr / (key + 1)) * (key + 1)
            print(ans)
        return ans

        