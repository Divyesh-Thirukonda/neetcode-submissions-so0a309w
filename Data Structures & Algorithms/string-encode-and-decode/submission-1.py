class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for st in strs:
            # if len(st) > 1000000000: return nuh uh
            strLen = str(len(st))
            strLenLen = str(len(strLen))
            ret += (strLenLen + strLen)
            ret += st
        return ret

    def decode(self, s: str) -> List[str]:
        # 210abcdefg tf12 a150abcd -> ["abcdefg tf", " a", "0abcd"]
        remaining = s[:]
        ret = []
        while len(remaining) != 0:
            print(remaining)
            strLenLen = int(remaining[0]) #2
            strLen = int(remaining[1:1+strLenLen]) #10
            header = 1 + strLenLen #3
            myStr = remaining[header : header + strLen]
            ret.append(myStr)
            remaining = remaining[header+strLen : ]
        return ret
        

        # you would need a string with 1000000000 chars to break this algo

