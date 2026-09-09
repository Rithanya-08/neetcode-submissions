from functools import lru_cache 
class Solution:
    @lru_cache(maxsize = None)
    def solve(self,s:str,i:int,op:int) -> bool:
        valid = False
        if i == len(s):
            return op == 0
        if(s[i] == "("):
            valid |= self.solve(s,i+1,op+1)
        elif(s[i] == "*"):
            valid |= self.solve(s,i+1,op+1)
            valid |= self.solve(s,i+1,op)
            if(op>0):
               valid |= self.solve(s,i+1,op-1)
        else:
            if(op>0):
                valid |= self.solve(s,i+1,op-1)

        return valid
            
    def checkValidString(self, s: str) -> bool:
        return self.solve(s,0,0)