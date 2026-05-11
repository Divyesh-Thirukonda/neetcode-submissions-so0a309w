class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ha = Counter(nums)
        bar = len(nums) / 3

        res = []
        
        for val, freq in ha.items():
            if freq > bar:
                res.append(val)
        return res