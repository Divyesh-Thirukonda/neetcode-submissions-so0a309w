class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        currMax = -10001
        theMaxBeforePop = -10001
        sol = []

        for i in range(len(nums)):
            if len(q) > 0 and q[0] <= i - k:
                q.popleft()
                
            while len(q) > 0 and nums[q[-1]] <= nums[i]:
                q.pop()
            
            q.append(i)
            if i >= k - 1:
                sol.append(nums[q[0]])
        return sol
