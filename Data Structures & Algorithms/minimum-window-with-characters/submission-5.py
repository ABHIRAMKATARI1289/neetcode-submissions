class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if not s or not t or len(s) < len(t):
            return ""

        need = {}
        for n in t:
            need[n] = need.get(n, 0) + 1

        window = {}
        have = 0
        needCount = len(need)

        res = ""
        reslen = float('inf')
        i = 0

        for j in range(len(s)):
            c = s[j]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    have += 1

            while have == needCount:
                if j - i + 1 < reslen:
                    res = s[i:j+1]
                    reslen = j - i + 1

                left = s[i]
                if left in need:
                    window[left] -= 1
                    if window[left] < need[left]:
                        have -= 1
                i += 1

        return res