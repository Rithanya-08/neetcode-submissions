class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(temp):
            if(len(temp) == len(nums)):
                result.append(temp[:])
                return

            for i in nums:
                if(i not in temp):
                    temp.append(i)
                    solve(temp)
                    temp.pop()

        solve([])
        return result