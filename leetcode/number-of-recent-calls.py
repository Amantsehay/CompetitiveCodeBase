class RecentCounter:

    def __init__(self):
        self.queue = []
        self.counter = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while t-self.queue[self.counter] > 3000:
            self.counter +=1
        
        return len(self.queue) - self.counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)