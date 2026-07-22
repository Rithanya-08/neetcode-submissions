class Solution:
    def eq(self,alp1 : dict,alp2:dict) -> bool:
        for num,count in alp2.items():
            if(alp1.get(num, 0)<count):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = l+len(t)-1
        change = True
        res = s + s
        alp2 = {} # For string t
        alp1 = {} # For string s

        if(len(s)<len(t)):
            return ""

        for j in t:
            if(j in alp2):
                alp2[j] += 1
            else:
                alp2[j] = 1

        for k in s[l:r]:
            if(k in alp2):
                if(k in alp1):
                    alp1[k] += 1
                else:
                    alp1[k] = 1

        while(r<len(s)):
            if(s[r] in alp2 and change == True):
                if(s[r] in alp1):
                    alp1[s[r]] +=1
                else:
                    alp1[s[r]] = 1

            change = False

            if(self.eq(alp1,alp2)):
                if(len(s[l:r+1])<len(res)):
                    res = s[l:r+1]
                if(s[l] in alp1):
                    if(alp1[s[l]] <2):
                        alp1.pop(s[l])
                    else:
                        alp1[s[l]] -=1
                l+=1
            else:
                r+=1
                change = True

        if(len(res) > len(s)):

            return ""
        else:
            return res

            



            




        

        