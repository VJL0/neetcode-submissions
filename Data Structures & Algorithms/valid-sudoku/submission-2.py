class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. row/col check
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in s:
                    return False
                s.add(board[j][i])

        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i+k][j+l]
                        if num == ".":
                            continue
                        if num in s:
                            return False
                        s.add(num)
                
        return True