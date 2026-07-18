class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^A-Za-z0-9]','',s)
        print(res)
        return res.lower() == res[::-1].lower()
        