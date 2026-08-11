class Solution:
    def dfs(self,grid: List[List[str]],i:int,j:int) -> None:
        rows = len(grid)
        cols = len(grid[0])
        if(i>=rows or i<0 or j<0 or j>=cols or grid[i][j] == "0"):
            return

        grid[i][j] = "0"

        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == "1"):
                    count += 1
                    self.dfs(grid,i,j)
        return count
                
        

        
        