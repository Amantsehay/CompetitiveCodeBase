class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rowHash, self.colHash, self.digHash = defaultdict(set), defaultdict(set), defaultdict(set)
        self.solved = False
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    self.rowHash[i].add(num)
                    self.colHash[j].add(num)
                    self.digHash[(i // 3) * 3 + j // 3].add(num)
        
        self.backtrack(board, 0, 0)

    def validate(self, i, j, val):
        boxid = (i // 3) * 3 + j // 3
        return val not in self.rowHash[i] and val not in self.colHash[j] and val not in self.digHash[boxid]

    def backtrack(self, board, i, j):
        if self.solved:
            return
        if i == 9:
            self.solved = True
            return
        if j == 9:
            self.backtrack(board, i + 1, 0)
            return

        if board[i][j] == ".":
            for num in map(str, range(1, 10)):
                if self.validate(i, j, num):
                    self.rowHash[i].add(num)
                    self.colHash[j].add(num)
                    self.digHash[(i // 3) * 3 + j // 3].add(num)
                    board[i][j] = num
                    self.backtrack(board, i, j + 1)
                    if not self.solved:
                        self.rowHash[i].remove(num)
                        self.colHash[j].remove(num)
                        self.digHash[(i // 3) * 3 + j // 3].remove(num)
                        board[i][j] = "."
        else:
            self.backtrack(board, i, j + 1)
