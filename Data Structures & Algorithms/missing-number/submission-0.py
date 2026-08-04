class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = sum(nums)
        n = len(nums)
        actual = (n*(n+1))//2

        return abs(actual - summ)

