class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs) == 1):
            return [strs]

        dic = {}

        for i in strs:
            p = "".join(sorted(i))
            if p in dic:
                dic[p].append(i)
            else:
                dic[p] = [i]
        
        return list(dic.values())

