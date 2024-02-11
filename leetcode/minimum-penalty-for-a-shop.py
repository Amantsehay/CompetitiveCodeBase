class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y=customers.count("Y")
        n=0
        final = 0
        ans=float("inf")
        for i in range(len(customers)):
            if ans > n  + y:
                final = i
                ans = n + y
            if customers[i]=="Y":
                y-=1
            else:
                n+=1

        if ans  > n + y:
            final = len(customers)
        
        return final
