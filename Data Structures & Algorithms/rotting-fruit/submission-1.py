class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        fresh = 0 

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 2):
                    queue.append((i,j))
                if(grid[i][j] == 1):
                    fresh+=1
        minutes = 0

        while(queue and fresh>0):
            size = len(queue)

            while(size):
                size -=1
                x,y = queue.pop(0)
                if(x+1<rows and grid[x+1][y] == 1 ):
                    queue.append((x+1,y))
                    grid[x+1][y] = 2
                    fresh -=1
                if(x-1 >= 0 and grid[x-1][y] == 1):
                    queue.append((x-1,y))
                    grid[x-1][y] = 2
                    fresh -=1
                if(y+1 < cols and grid[x][y+1] == 1):
                    queue.append((x,y+1))
                    grid[x][y+1] = 2
                    fresh -=1
                if(y-1>=0 and grid[x][y-1] == 1):
                    queue.append((x,y-1))
                    grid[x][y-1] = 2
                    fresh -=1
            minutes += 1

        if(fresh == 0):
            return minutes
        else:
            return -1

                

            

        

