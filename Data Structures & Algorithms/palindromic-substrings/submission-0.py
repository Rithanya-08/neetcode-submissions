class Solution:
    def countSubstrings(self, s: str) -> int:
        result = []
        count = 0
        
        def palindrome(s):
            return s == s[::-1]

        def solve(i,temp):
            nonlocal count 
            if(i == len(s)):
                result.append("".join(temp))
                return

            for j in range(i,len(s)):
                if(palindrome(s[i:j+1])):
                    count+=1

        for i in range(len(s)):
            solve(i,[])
        return count
        