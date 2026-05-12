class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        n = len(nums)
        idx = {}

        target = 0

        for i, num in enumerate(nums):
            if not num in idx:
                idx[num] = []
            idx[num].append(i)

        for i in range(n):
            ni = nums[i]
            
            for j in range(i+1, n):
                rem = target - ni - nums[j]

                if rem in idx:
                    for k in idx[rem]:
                        if (not k == i) and (not k == j):
                            subsol = sorted([nums[i], nums[j], nums[k]])
                            res.add(tuple(subsol))
        return [list(i) for i in res]


                


        