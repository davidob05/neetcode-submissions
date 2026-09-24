# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode(0, head)
        cur, prev = head, dummy
        count = 0
        while cur:
            cur = cur.next
            if count == n:
                prev = prev.next
            else:
                count += 1
        prev.next = prev.next.next
        return dummy.next