class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        n = len(word)
        seen = set()


        def dfs(row, col, idx):
            if idx == len(word):
                return True
            
            if (
                (row, col) in seen 
                or row < 0 or col < 0 
                or col >= cols or row >= rows 
                or word[idx] != board[row][col]
            ):
                return False

            seen.add((row, col))

            res = (
                dfs(row + 1, col, idx + 1) or 
                dfs(row, col + 1, idx + 1) or 
                dfs(row - 1, col, idx + 1) or 
                dfs(row, col - 1, idx + 1) 
            )
            seen.remove((row, col))
            return res


        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False