class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        land = 0
        queue = []
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 2147483647):
                    land += 1
                if(grid[i][j] == 0):
                    queue.append((i,j))

        while(queue and land >0):
            x,y = queue.pop(0)
            if(x+1<rows and grid[x+1][y] == 2147483647):
                grid[x+1][y] = grid[x][y] +1
                queue.append((x+1,y))
                land-=1
            if(x-1>=0 and grid[x-1][y] == 2147483647):
                grid[x-1][y] = grid[x][y] +1
                queue.append((x-1,y))
                land-=1
            if(y-1>=0 and grid[x][y-1] == 2147483647):
                grid[x][y-1] = grid[x][y] +1
                queue.append((x,y-1))
                land-=1
            if(y+1<cols and grid[x][y+1] == 2147483647):
                grid[x][y+1] = grid[x][y] +1
                queue.append((x,y+1))
                land-=1

        return

        



