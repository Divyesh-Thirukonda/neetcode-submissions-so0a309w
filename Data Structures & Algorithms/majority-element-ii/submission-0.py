class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ha = Counter(nums)
        bar = len(nums) / 3
        sol = []
        for k,v in ha.items():
            if v > bar:
                sol.append(k)
        return sol