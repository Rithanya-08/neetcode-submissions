class Solution:
    def dfs(self, grid: List[List[int]], i : int , j:int) -> int :

        rows = len(grid)
        cols = len(grid[0])
        if(i<0 or i>= rows or j<0 or j>= cols or grid[i][j] == 0):
            return 0 

        grid[i][j] = 0
        
        count = 1
         
        count += self.dfs(grid,i+1,j)
        count += self.dfs(grid,i-1,j)
        count += self.dfs(grid,i,j+1)
        count += self.dfs(grid,i,j-1)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxx = 0 
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 1):
                    count =0
                    count = self.dfs(grid,i,j)
                    maxx = max(maxx,count)
        return maxx