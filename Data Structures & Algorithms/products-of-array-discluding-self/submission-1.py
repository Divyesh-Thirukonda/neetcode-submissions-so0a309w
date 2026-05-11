class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,3,4]

        [1,2,6,24]
        [24,24,12,4]
        1*24
        1*12
        2*4
        6*1
        '''

        left = [1]
        for n in nums:
            left.append(left[-1]*n)
        
        right = [1]
        for n in nums[::-1]:
            right.append(right[-1]*n)
        
        print(left)
        print(right)

        res = []

        n = len(nums)
        for i in range(n):
            l = i
            r = n-i-1
            res.append(left[l]*right[r])



        return res


