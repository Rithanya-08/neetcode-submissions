class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def solve(temp,op,close):
            if(len(temp) == 2*n):
                result.append("".join(temp))
                return

            if(op<n):
                temp.append("(")
                solve(temp,op+1,close)
                temp.pop()
            if(close<op):
                temp.append(")")
                solve(temp,op,close+1)
                temp.pop()

        solve([],0,0)

        return result