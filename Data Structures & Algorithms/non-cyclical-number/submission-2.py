class Solution:
    def check(self,n:int)->int:
        temp=n
        s=0
        while(temp>0):
            last=temp%10
            temp=temp//10
            s+=last*last
        return s
    def isHappy(self, n: int) -> bool:
        visited = set()
        while(True):
            if(n==1):
                return True
            if(n in visited):
                return False
            else:
                visited.add(n)
                n =      self.check(n)
