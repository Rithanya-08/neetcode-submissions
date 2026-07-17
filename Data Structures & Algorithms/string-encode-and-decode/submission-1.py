class Solution:

    def decode(self, s: str) -> List[str]:
        lst = []
        p = 0

        while(p<len(s)):
            temp = p
            while(s[p]!='#'):
                p+=1
            leng = int(s[temp:p])
            if(leng == 0):
                word = ""
                p+=1
            else:
                word = s[p+1:p+1+leng]
                p += leng+1
            lst.append(word)

        return lst


    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "#" + i

        return encoded
