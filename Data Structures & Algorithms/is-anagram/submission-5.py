class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        ht = {}
        for cs in s:
                if cs in hs.keys():
                    hs[cs] += 1
                else:
                    hs[cs] = 1
        for ct in t:
            if ct in ht.keys():
                ht[ct] += 1
            else:
                ht[ct] = 1
        return hs == ht