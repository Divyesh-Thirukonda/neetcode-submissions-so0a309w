# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        length = len(nodes)
        idx = length - n

        # removing head
        if idx == 0:
            return head.next

        # bypass the nth-from-end node
        nodes[idx - 1].next = nodes[idx].next

        return head