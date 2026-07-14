class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h1 = {}
        for n in nums :
            h1[n] = h1.get(n,0) + 1 
            if h1[n] > 1 :
                return True
        return False 
        