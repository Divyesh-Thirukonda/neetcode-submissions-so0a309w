class Solution:
    def checkValidString(self, s: str) -> bool:
        minn, maxx = 0,0
        for c in s:
            if c == "(":
                minn += 1
                maxx += 1
            elif c == ")":
                minn -= 1
                maxx -= 1
            else:
                minn -= 1
                maxx += 1
            
            if maxx < 0:
                return False
            
            if minn < 0:
                minn = 0
                

        return minn == 0



        # -1 3

