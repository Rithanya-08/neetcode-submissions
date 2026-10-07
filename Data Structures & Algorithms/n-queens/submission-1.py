class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        result = []
        columns = []
        diag = []
        anti_diag = []
        def safe(row,col):
            if col in columns:
                return False

            if row + col in diag:
                return False

            if row - col in anti_diag:
                return False

            return True
        
        def solve(board,row):
            if(row>=n):
                result.append(["".join(p) for p in board])
                return 
            for col in range(n):
                if(safe(row,col)):
                    columns.append(col)
                    diag.append(row+col)
                    anti_diag.append(row-col)

                    board[row][col] = "Q"
                    solve(board,row+1)
                    board[row][col] = "."

                    columns.pop()
                    diag.pop()
                    anti_diag.pop()

        solve(board,0)
        return result

            
