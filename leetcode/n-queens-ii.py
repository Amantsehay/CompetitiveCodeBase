class Solution:

    def totalNQueens(self, n: int) -> int:
        self.sumSet, self.diffSet, self.iSet, self.jSet = set(), set(), set(), set()
        self.ans = 0
        def validate(i, j):
            if ( (i + j not in  self.sumSet) and (i - j not in self.diffSet) and (i) not in self.iSet and j not in self.jSet):
                return True
            return False
        def backtrack(idx):
            if idx >= n:
                self.ans += 1
                return 
            for j in range(n):
                if validate(idx, j):
                    self.sumSet.add( idx+ j)
                    self.diffSet.add(idx - j)
                    self.iSet.add(idx) 
                    self.jSet.add(j)
                    backtrack(idx + 1)
                    self.sumSet.remove( idx+ j)
                    self.diffSet.remove(idx - j)
                    self.iSet.remove(idx) 
                    self.jSet.remove(j)
            
        backtrack(0)
        return self.ans


        