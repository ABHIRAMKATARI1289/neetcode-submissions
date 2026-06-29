class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        res = ""
        for n in s :
            if n.isalnum():
                res += n.lower()
        return res == res[::-1]