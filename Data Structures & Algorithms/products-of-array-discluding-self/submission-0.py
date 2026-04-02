class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        [1, 2, 4, 6]

        # L0 = 1
        # L1 = 1
        # L2 = 2
        # L3 = 8

        # R0 = 48
        # R1 = 24
        # R2 = 6
        # R3 = 1

        n = len(nums)

        left = [1]
        for i in range(n - 1):
            left.append(left[-1] * nums[i])

        right = [1]
        for i in range(n - 1, 0, -1):
            right.append(right[-1] * nums[i])

        res = []
        for i in range(n):
            res.append(left[i] * right[n - 1 - i])

        return res
