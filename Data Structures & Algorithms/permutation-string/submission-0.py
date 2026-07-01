class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp = Counter(s1)
        n = len(s1)
        
        for i in range(len(s2)):
            if Counter(s2[i:i+n]) == temp :
                return True 
        return False 