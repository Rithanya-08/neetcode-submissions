class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        for i in range(31,-1,-1):
            digit = n >> i
            if(digit & 1 == 1):
                count += 1

        return count
