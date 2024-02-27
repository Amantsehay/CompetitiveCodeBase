class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        

        # using two queues just 
        d, r = deque(), deque()
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == "D":
                d.append(i)
            else:
                r.append(i)
        
        while d and r:
            if d[0] < r[0]:
                r.popleft()
                d.append(d.popleft() + n)
            else:
                d.popleft()
                r.append(r.popleft() + n)
        if d:
            return "Dire"
        else:
            return "Radiant"
