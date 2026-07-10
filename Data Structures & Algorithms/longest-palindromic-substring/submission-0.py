class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def calc(s,l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1 
            return r-l-1
        
        start = 0 
        end = 0 

        for i in range(n):
            even = calc(s,i,i+1)
            odd = calc(s,i,i)
            maxim = max(even,odd)

            if maxim > end - start :
                start = i - (maxim-1)//2
                end = i + maxim//2
        return s[start:end+1]
        
        