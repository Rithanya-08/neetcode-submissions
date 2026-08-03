class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [] 
        carry = 0 
        last = digits[-1] + 1
        first = True
        if(last >= 10):
            for i in digits[::-1]:
                if(first == True):
                    dig = (i + 1) % 10
                    carry = (i+1) // 10
                    result.append(dig)
                    first = False
                else:
                    dig = (i + carry) % 10
                    carry = (i+carry) // 10
                    result.append(dig)

            if(carry != 0):
                result.append(carry)
            
            result.reverse()
            return result

                

        else:
            digits[-1] = last 
            result = digits
            return result

