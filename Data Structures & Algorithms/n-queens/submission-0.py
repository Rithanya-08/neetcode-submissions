class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        result = []


        def safe(board,row,col):
            for i in range(row):
                if(board[i][col] == "Q"):
                    return False
            i = row-1
            j = col+1
            # Right diagonal
            while(i>=0 and j<n):
                if(board[i][j] == "Q"):
                    return False
                i-=1
                j+=1
            
            i = row-1
            j = col-1
            # Left diagonal
            while(i>=0 and j>=0):
                if(board[i][j] == "Q"):
                    return False
                i-=1
                j-=1

            return True

        def solve(board,row):
            if(row>=n):
                result.append(["".join(p) for p in board])
                return 
            for col in range(n):
                if(safe(board,row,col)):
                    board[row][col] = "Q"
                    solve(board,row+1)
                    board[row][col] = "."

        solve(board,0)
        return result

            
