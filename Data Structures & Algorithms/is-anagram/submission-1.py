class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        if len(s) != len(t) :
            return False 

        for n in s :
            h1[n] = h1.get(n,0) + 1 
        for n in t :
            h2[n] = h2.get(n,0) + 1
        for n in s :
            if n not in h2 or h1[n] != h2[n] :
                return False
        return True 

        