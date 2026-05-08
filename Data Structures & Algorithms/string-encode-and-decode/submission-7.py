class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = str(len(s))
            res += n
            res += "#"
            res += s
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sol = []
        i = 0
        while i < len(s):
            c = 0
            howFar = ""
            while s[i] != "#":
                howFar += s[i]
                i += 1
                c += 1
            howFar = int(howFar)
            word = s[i+1 : i+howFar+1]
            sol.append(word)
            i += howFar+1
        return sol
