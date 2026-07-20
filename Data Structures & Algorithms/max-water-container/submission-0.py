class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l = 0
        r = n-1
        water = 0
        maxx = 0

        while(l<r):
            water = min(heights[l],heights[r]) * (r-l)
            maxx = max(maxx,water)

            if(heights[l]<=heights[r]):
                l+=1
            else:
                r-=1
                          


        return maxx



            
        