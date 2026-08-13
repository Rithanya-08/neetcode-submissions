class Solution:
    def dfs(self,heights: List[List[int]], stack:list ,pacific : bool, atlantic : bool) -> bool:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        rows = len(heights)
        cols = len(heights[0])
        
        visited = []
        visited.append(list(stack[-1]))

        while(stack):
            x,y = stack.pop()


            for nx,ny in directions:
                if(x+nx < 0 or y+ny<0):
                    pacific = True
                if(x+nx >= rows  or y+ny >= cols):
                    atlantic = True
                if(x+nx >= 0 and  y+ny>=0 and x+nx < rows  and y+ny < cols):
                    if(heights[x+nx][y+ny] <= heights[x][y] and [x+nx,y+ny] not in visited):
                        stack.append((x+nx, y+ny))
                        visited.append([x+nx, y+ny])
                
        
        return pacific and atlantic

            


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        result = []
        
        for i in range(rows):
            for j in range(cols):
                pacific = False
                atlantic = False
                stack = [(i,j)]

                both = self.dfs(heights,stack,pacific,atlantic)
                if(both == True):
                    result.append([i,j])

        return result


                