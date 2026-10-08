class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {}
        dic[2] = "abc"
        dic[3] = "def"
        dic[4] = "ghi"
        dic[5] = "jkl"
        dic[6] = "mno"
        dic[7] = "pqrs"
        dic[8] = "tuv"
        dic[9] = "wxyz"
        result = []

        def solve(i,temp):
            if(i == len(digits)):
                result.append("".join(temp))
                return 
            nums = int(digits[i])
            for ch in dic[nums]:
                temp.append(ch)
                solve(i+1,temp)
                temp.pop()
        if(digits == ""):
            return []
        solve(0,[])
        return result

        