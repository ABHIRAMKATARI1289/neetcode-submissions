class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(i,open,close,s):
            if i == 2 * n and open == close :
                res.append(s)
                return 
            if open < n :
                dfs(i + 1, open + 1 ,close, s + "(")
            if close < open:
                dfs(i + 1, open, close + 1, s + ")")
        res = []
        dfs(0,0,0,"")
        return res


            
            
            
            
        