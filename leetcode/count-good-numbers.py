class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = math.ceil(n /2)
        odd = n //2
        mod = 10**9 + 7
        memo = {}
        memo2 = {}
        return (self.pow(5, even, memo) * self.pow(4, odd, memo2)) % mod
       

    def pow(self, n, p, memo):
        mod = 10**9 + 7
        if p == 0:
            return 1
        if p in memo:
            return memp[p]
        
        x = self.pow(n, p//2, memo)
        val = 0
        if p % 2 == 0:
            val =  (x * x) % mod
        else:
            val  = (n * x * x) % mod
        memo[p] =  val
        return val


