class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []


    def push(self, val: int) -> None:

        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)

        elif(self.minstack[-1]>val):
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
               

    def top(self) -> int:
        temp = self.stack.pop()
        self.stack.append(temp)
        return temp
        

    def getMin(self) -> int:
        return self.minstack[-1]
       



        
