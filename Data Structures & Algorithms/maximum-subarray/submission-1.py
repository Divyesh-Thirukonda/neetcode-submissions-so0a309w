class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = -1001
        currMax = -1001
        for n in nums:
            currMax = max(currMax, 0)
            currMax += n
            maxSoFar = max(maxSoFar, currMax)
        return maxSoFar