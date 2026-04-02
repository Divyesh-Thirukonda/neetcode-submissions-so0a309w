# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l1

        carry = False
        prev = None
        while l1 or l2 or carry:
            if not l1:
                prev.next = ListNode(0)
                l1 = prev.next
            newV = ((l1.val if l1 else 0) + (l2.val if l2 else 0))
            if carry:
                newV += 1
            if newV > 9:
                newV = newV % 10
                carry = True
            else:
                carry = False
            l1.val = newV

            prev = l1
            l1 = l1.next
            l2 = l2.next if l2 else None
        

        return dummy



