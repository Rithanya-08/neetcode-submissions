class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        result = []
        start = 0
        end = 0 
        for i in range(len(s)-1,-1,-1):
            if(s[i] not in dic):
                dic[s[i]] = i

        for i in range(len(s)):
            end = max(end,dic[s[i]])

            if(end == i):
                result.append(end - start+1)
                start = i + 1
                end = i + 1

        return result