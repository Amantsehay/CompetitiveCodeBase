class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.sumSet, self.diffSet, self.iSet, self.jSet = set(), set(), set(), set()
        self.ans = []
        self.curr = []
        def validate(i, j):
            if ( (i + j not in  self.sumSet) and (i - j not in self.diffSet) and (i) not in self.iSet and j not in self.jSet):
                return True
            return False
        def backtrack(idx):
            if idx >= n:
                self.ans.append(self.curr[:])
                return 
            for j in range(n):
                if validate(idx, j):
                    self.sumSet.add( idx+ j)
                    self.diffSet.add(idx - j)
                    self.iSet.add(idx) 
                    self.jSet.add(j)
                    self.curr.append(j)
                    backtrack(idx + 1)
                    self.sumSet.remove( idx+ j)
                    self.diffSet.remove(idx - j)
                    self.iSet.remove(idx) 
                    self.jSet.remove(j)
                    self.curr.pop()
            
        backtrack(0)
        result = []
        for i in range(len(self.ans)):
            ith = []
            for idx in self.ans[i]:
                s = ["."] * n
                s[idx] = "Q"
                ith.append("".join(s))
            result.append(ith)
        return result
            





        
        