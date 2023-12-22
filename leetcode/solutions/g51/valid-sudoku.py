class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # box number = (i //3) * 3 + j//3
        n = len(board)
        columnMap = [set() for _ in range(n)]
        rowMap = [set() for _ in range(n)]
        boxMap = {}
        for i in range(n):
            for j in range(n):
                currNum = board[i][j]
                if currNum != ".":
                    if currNum in columnMap[j] or  currNum in rowMap[i]:
                        return False
                    columnMap[j].add(currNum)
                    rowMap[i].add(currNum)

                    boxid = (i//3) * 3 + j//3
                    if (boxid in boxMap):
                        if currNum in boxMap[boxid]:
                            return False
                        else:
                            boxMap[boxid].add(currNum)
                    else:
                        boxMap[boxid] = set(currNum)
        return True
