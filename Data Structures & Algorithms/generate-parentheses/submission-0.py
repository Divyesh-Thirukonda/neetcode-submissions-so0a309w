class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add for each

        # maintain:
        # numOpen <= n
        # numOpen >= numClose

        self.valid = []

        
        def rec(s, openCount, closeCount):
            if openCount == n and closeCount == n:
                self.valid.append(s)
                return
            
            if openCount < n:
                rec(s + "(", openCount + 1, closeCount)
            if openCount > closeCount:
                rec(s + ")", openCount, closeCount + 1)
            
        rec("", 0, 0)

        return self.valid
