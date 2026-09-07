from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def check(self, n: int, c:int) -> int:
        
        if(c == n):
            return 1
        if(c>n):
            return 0

        return self.check(n,c+1) + self.check(n,c+2)


    def climbStairs(self, n: int) -> int:
        return self.check(n,0)




            
            