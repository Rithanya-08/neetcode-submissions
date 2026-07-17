class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unique = {}
        if(len(s)!=len(t)):
            return False
        for i in s:
            if i not in unique:
                unique[i] = 1
            else:
                unique[i]+=1

        for i in t:
            if i not in unique:
                return False
            else:
                unique[i]-=1
        
        for c in unique.values():
            if c != 0 :
                return False
        return True
