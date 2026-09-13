class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        
        n = len(s)

        h1 = defaultdict(int)
        h2 = defaultdict(int)
        for i in range(n):
            h1[s[i]] += 1 
            h2[t[i]] += 1 
        
        for j in s :
            if h1[j] != h2[j]:
                return False 
        return True 