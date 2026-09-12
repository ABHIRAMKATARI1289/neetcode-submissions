class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h1 = set()
        for n in nums:
            if n in h1 :
                return True 
            h1.add(n)
        return False 