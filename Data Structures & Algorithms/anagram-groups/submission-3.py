class Solution:
    def discover(self,s:str):
        alp = [0]*26
        for i in s:
            alp[ord(i)-97]+=1

        new = ""
        for j in range(len(alp)):
            if(alp[j]>0):
                new += (chr(97+j)) * alp[j]

        return new

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        for p in strs:
            word = self.discover(p)

            if word not in dic:
                dic[word] = [p]
            else:
                dic[word].append(p)

        return list(dic.values())

        