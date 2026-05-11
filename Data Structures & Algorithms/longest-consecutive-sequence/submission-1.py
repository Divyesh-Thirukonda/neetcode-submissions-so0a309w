class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for n in nums:
            curr = n
            while curr + 1 in seen:
                curr += 1
            longest = max(longest, curr - n + 1)
        return longest