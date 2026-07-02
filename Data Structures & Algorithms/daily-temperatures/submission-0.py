class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) 
        res = []
        for i in range(n):
            cnt = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break 
                j += 1
                cnt += 1
            if j == n :
                cnt = 0
            res.append(cnt)
        return res 