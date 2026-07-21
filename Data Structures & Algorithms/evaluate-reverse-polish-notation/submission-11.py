class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        for i in tokens:
            print(stack)
            if i not in "+-*/":
                stack.append(int(i))
            else:
                x = stack.pop()
                y = stack.pop()


                if(i == '+'):
                    stack.append(x+y)
                elif(i =='-'):
                    stack.append(y-x)
                elif(i == '*'):
                    stack.append(x*y)
                else:
                    if(x!=0):
                        stack.append(int(y/x))

        if stack:
            return int(stack[-1])
        else:
            return 0
                