class Solution:
    def isValid(self, s: str) -> bool:
        if not s :
            return True 
        stack = []
        par = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for n in s :
            if n in par.keys() and stack:
                if par[n] != stack.pop():
                    return False 
            else :
                stack.append(n)
        if stack :
            return False
        return True 

        