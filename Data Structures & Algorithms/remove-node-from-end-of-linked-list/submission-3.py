# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        runUp = []
        cur = head

        while cur:
            runUp.append(cur)
            cur = cur.next

        length = len(runUp)
        idx = length - n

        if idx <= 0:
            return head.next  

        runUp[idx - 1].next = runUp[idx].next

        return head

