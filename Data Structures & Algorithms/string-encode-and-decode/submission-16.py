class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        concat = ""
        for s in strs:
            n = len(s)
            encoded += str(n)
            encoded += ","
            concat += s
        encoded += "#"
        encoded += concat
        return encoded


    def decode(self, s: str) -> List[str]:
        lens = [","]

        split = s.find("#") + 1
        words = s[split:]

        for lenWord in s:
            if lenWord == "#":
                break
            if lens[-1] != ",":
                if lenWord != ",":
                    lens[-1] *= 10
                    lens[-1] += int(lenWord)
                else:
                    lens.append(",")
            else:
                lens.append(int(lenWord))
        lens = [el for el in lens if el != ","]

        result = []

        i = 0
        for elem in lens:
            result.append(words[i:i+elem])
            i += elem
            

        return result

