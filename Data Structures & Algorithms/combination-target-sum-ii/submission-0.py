class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i,total,fin):
            if total == target :
                res.append(fin.copy())
                return 
            elif i >= len(candidates):
                return  
            elif total > target :
                return 

            fin.append(candidates[i])
            dfs(i+1,total + candidates[i],fin)
            fin.pop()
            j = i + 1 
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j,total,fin)

        candidates.sort()
        res = []
        dfs(0,0,[])
        return res         