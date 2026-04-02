class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ha = set()
        for el in nums:
            if el in ha:
                return True
            else:
                ha.add(el)
        return False