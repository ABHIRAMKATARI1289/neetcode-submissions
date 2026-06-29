class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        res = []
        for n in s :
            if n.isalnum():
                res.append(n.lower())
        print(res)
        r = len(res) - 1
        while l <= r:
            if res[l] != res[r] :
                return False 
            l +=1 
            r -= 1
        return True 
        