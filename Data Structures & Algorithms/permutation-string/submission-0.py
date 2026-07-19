class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alp1 = [0]*26
        alp2 = [0]*26

        n1 = len(s1)

        i = 0 
        j = n1-1

        for el1 in s1:
            alp1[ord(el1)-ord('a')] += 1

        
        for el2 in s2[i:j+1]:
            alp2[ord(el2)-ord('a')] += 1


        while(j<len(s2)):                    
            if(alp1 == alp2):
                return True

            alp2[ord(s2[i]) - ord('a')] -= 1
            i+=1
            j+=1
            if(j<len(s2)):
                alp2[ord(s2[j]) - ord('a')] += 1

        return False
