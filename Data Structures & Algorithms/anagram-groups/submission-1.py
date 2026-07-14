class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h1 = defaultdict(list)
        for i,word in enumerate(strs):
            l = sorted(word)
            h1["".join(sorted(word))].append(strs[i])
        return list(h1.values())