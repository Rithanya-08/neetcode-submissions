class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            digit = n >> i
            if(digit & 1 ==1):
                res = (res << 1) | 1
            else:
                res = (res << 1) | 0 

        return res

        