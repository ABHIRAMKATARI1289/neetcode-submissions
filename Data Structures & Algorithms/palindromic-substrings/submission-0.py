class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def calc(s,l,r):
            cnt = 0 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1
                cnt += 1
            return cnt 
        
        for i in range(len(s)):
            res  += calc(s,i,i)
            res  += calc(s,i,i+1)
        return res

        