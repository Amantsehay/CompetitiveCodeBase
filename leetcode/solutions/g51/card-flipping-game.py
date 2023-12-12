from collections import Counter

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # So the quesitons is can you move the cards
        counter = Counter(fronts)
        counter2 = Counter(backs)
        ans1 = self.check(counter, fronts, backs)
        ans2 = self.check(counter2, backs, fronts)
        if ans1 == 0 and ans2 == 0:
            return 0
        elif ans1 == 0:
            return ans2
        elif ans2 == 0: 
            return ans1
        else:
            return min(ans1, ans2)

    def check(self, counter, fronts, backs):

        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                counter[fronts[i]] -=1
        ans = float("inf")
        for key in counter:
            if counter[key] == 0 and key < ans:
                ans = key
        return ans if ans != float("inf") else 0
            
        
        