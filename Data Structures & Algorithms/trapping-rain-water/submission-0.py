class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        leftmax = 0
        rightmax = 0
        h = 0

        
        while(l<r):
            if(height[l]<height[r]):
                if(height[l]>leftmax):
                    leftmax = height[l]
                else:
                    h += leftmax- height[l]
                l+=1
            else:
                if(height[r]>rightmax):
                    rightmax = height[r] 
                else:
                    h+= rightmax - height[r]
                r-=1
        return h  


