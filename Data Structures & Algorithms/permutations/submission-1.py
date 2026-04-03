class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                bt(i+1, curr)
                nums[i], nums[j] = nums[j], nums[i]
        bt(0, nums)
        return res