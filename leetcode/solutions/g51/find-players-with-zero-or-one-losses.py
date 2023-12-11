class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        ans2 = []
        loss = {}
        for match in matches:
            winner = match[0]
            loser = match[1]
            loss[winner] = loss.get(winner, 0) 
            loss[loser] = loss.get(loser, 0) + 1
        for player in loss:
            if loss[player] == 1:
                ans.append(player)
            if loss[player] == 0:
                ans2.append(player)
        ans.sort()
        ans2.sort()

        return [ ans2, ans]

                





        