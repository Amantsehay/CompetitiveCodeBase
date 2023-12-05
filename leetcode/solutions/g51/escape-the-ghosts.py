class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # if the ghost arrives first then we're done 
        turns = abs(target[0]) + abs(target[1]) 
        for i in range(len(ghosts)):
            need = abs(ghosts[i][0] - target[0])  + abs(ghosts[i][1] - target[1])
            if (need <= turns):
                return False
        return True

        