class Solution:
    def palindormeCheck(self,s:str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        dp = [""]*(len(s))

        for i in range(len(s)):
            for j in range(i+1):
                if(self.palindormeCheck(s[j:i+1])):
                    if len(s[j:i+1]) > len(dp[i]):
                        dp[i] = s[j:i+1]

                        
        return max(dp, key=len)