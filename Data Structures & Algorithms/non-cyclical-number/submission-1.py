class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfDigsSq(n):
            summ = 0
            while n > 0:
                mod = n % 10
                n = n // 10
                summ += (mod**2)

            return summ
        currDigsSum = sumOfDigsSq(n)
        seen = set()

        while currDigsSum not in seen:
            if currDigsSum == 1:
                return True
            seen.add(currDigsSum)
            currDigsSum = sumOfDigsSq(currDigsSum)
        return False
            