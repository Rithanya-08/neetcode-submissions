class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        match = {}

        for i in range(len(position)):
            match[position[i]] = speed[i]

        sorted_dic = dict(sorted(match.items(),reverse = True))
        stack = []
        
        for i in sorted_dic:
            time = (target - i)/sorted_dic[i]
            stack.append(time)
            if(len(stack)> 1 and stack[-1]<=stack[-2]):
                stack.pop()
            
        return len(stack)