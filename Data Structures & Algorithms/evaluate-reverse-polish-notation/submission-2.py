class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda a,b : int(a) + int(b) ,
            '-': lambda a,b : int(a) - int(b) ,
            '*': lambda a,b : int(a) * int(b) ,
            '/': lambda a,b : int(int(a)/int(b))
        }
        stack = []
        for n in tokens :
            if n in ops :
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[n](a,b))
            else :
                stack.append(int(n))
        return stack[-1]
        