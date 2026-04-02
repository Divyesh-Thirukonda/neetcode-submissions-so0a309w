class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDiffs = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seenDiffs:
                return [seenDiffs[diff], i]
            else:
                seenDiffs[n] = i
        return []