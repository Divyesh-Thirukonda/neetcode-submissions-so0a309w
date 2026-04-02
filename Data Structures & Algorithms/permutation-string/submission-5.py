class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1C = Counter(s1)
        # s2C = Counter(s2)

        left = 0
        right = len(s1)



        while right <= len(s2):
            for i in range(left, right):
                if s2[i] in s1C.keys():
                    s1C[s2[i]] -= 1

            vals = [False if val > 0 else True for val in s1C.values()]
            print(s2[left:right])
            print(vals)
            print(s1C)

            if not False in vals:
                return True
            left += 1
            right += 1
            s1C = Counter(s1)
        return False



        

