class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h1 = defaultdict(list)
        for s in strs :
            h1[''.join(sorted(s))].append(s)
        return list(h1.values())