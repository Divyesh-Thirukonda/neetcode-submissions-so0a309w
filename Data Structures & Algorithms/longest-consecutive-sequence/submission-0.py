class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        res = 0

        for i in range(len(nums)):

            if nums[i] - 1 not in s:

                c = 1
                while nums[i] + c in s:
                    c += 1
                res = max(res, c)
        return res