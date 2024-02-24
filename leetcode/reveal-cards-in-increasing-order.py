class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()
        n = len(deck)
        queue = deque([i for i in range(n)])
        ans = [0] * n
        print(queue)
        for i in range(n):
            ans[queue.popleft()] = deck[i]
            if queue:
                queue.append(queue.popleft())
        print(ans)
        return ans