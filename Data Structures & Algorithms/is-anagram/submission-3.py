class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1 = defaultdict(int)
        for n in s :
            h1[n] += 1 
        
        for n in t :
            if h1[n] == 0:
                return False 
            h1[n] -= 1 
        return True 