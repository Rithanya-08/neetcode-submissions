class Solution:
    def isSafe(self,board: List[List[str]],i,j,target) -> bool:
        visited = False
        for ele in board[i]:
            if(ele == target and visited == False):
                visited = True
            elif(ele == target and visited == True):
                return False

        visited = False
        for p in range(0,9):
            if(board[p][j] == target and visited == False):
                visited = True
            elif(board[p][j] == target and visited == True):
                return False

            
        visited = False
        box_x = (i//3)*3
        box_y = (j//3)*3

        for a in range(box_x,box_x+3):
            for b in range(box_y,box_y+3):
                if(board[a][b] == target and visited == False):
                    visited = True
                elif(board[a][b] == target and visited == True):
                    return False

        return True
                

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j]!="."):
                    if not self.isSafe(board,i,j,board[i][j]):
                        return False

        return True
        
        
        