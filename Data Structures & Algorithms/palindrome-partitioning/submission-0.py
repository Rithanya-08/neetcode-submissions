class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def palindrome(s):
            return s == s[::-1]
        def solve(i,temp):
            if(i == len(s)):
                result.append(temp[:])
                return 
            for j in range(i,len(s)):
                if(palindrome(s[i:j+1])):
                    temp.append(s[i:j+1])
                    solve(j+1,temp)
                    temp.pop()
        solve(0,[])
        return result
