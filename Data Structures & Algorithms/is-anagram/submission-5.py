class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        h1 = defaultdict(int)
        h2 = defaultdict(int)
        for n in s :
            h1[n] += 1 
        for n in t :
            h2[n] += 1 

        for n in s :
            if h1[n] != h2[n] :
                return False 
        return True 