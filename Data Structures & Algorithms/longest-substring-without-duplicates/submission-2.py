class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dic = {}
        maxx = 0
        i = 0
        j = 0
        while j<len(s):
            if s[j] in dic:
                rep = dic[s[j]]
                i = max(rep + 1,i)
            dic[s[j]] = j
            maxx = max(maxx,j-i+1)
            j+=1
        return maxx



            
