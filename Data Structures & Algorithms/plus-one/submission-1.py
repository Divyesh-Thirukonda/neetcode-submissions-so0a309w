class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        for d in range(len(digits) - 1, -1, -1):
            digits[d] += carry
            if digits[d] > 9:
                digits[d] = 0
                carry = 1
            else:
                carry = 0
            print(d)
        if carry:
            digits.insert(0, 1)
        return digits