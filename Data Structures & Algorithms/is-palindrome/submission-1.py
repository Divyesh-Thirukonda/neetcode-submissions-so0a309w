class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        n = len(s)
        # print(s)
        for i in range(len(s)//2):
            if s[i] != s[n - i - 1]:
                # print(i, s[n-i-1])
                return False
        # for c in s:
        #         newStr += c.lower()
        return True        