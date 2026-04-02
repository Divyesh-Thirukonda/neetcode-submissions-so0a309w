class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            hoursSpent = sum([(p+k-1)//k for p in piles])

            if hoursSpent <= h:
                # found valid, keep going lower k
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
        # .
        # .
        # .
        # k = 2 -> 6
        # .
        # .
        # .
        # kMin = 1
        # kMax = max(piles)



