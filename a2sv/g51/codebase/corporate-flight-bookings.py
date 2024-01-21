class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        
        dp = [0] * n 
        m = len(bookings)

        for i in range(m):
            first, last, seats = bookings[i]
            dp[first -1] += seats
            if last < n:
                dp[last] -= seats

        for i in range(1, n):
            dp[i] += dp[i - 1]
        return dp


        