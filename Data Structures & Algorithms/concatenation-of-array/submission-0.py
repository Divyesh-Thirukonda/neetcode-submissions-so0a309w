class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*(n*2)
        for i, curr in enumerate(nums):
            res[i] = curr
            res[i+n] = curr
        return res