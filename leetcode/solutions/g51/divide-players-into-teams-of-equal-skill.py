class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        i = 0
        j = n - 1
        skill.sort()
        first = skill[i] + skill[j]
        ans = 0
        while i < j:
            if skill[i] + skill[j] == first:
                ans += skill[i] * skill[j]
            else:
                return -1
            i += 1
            j -= 1
        return ans
        