# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        if head is not None:
            next_node = head.next

        while curr!=None:
            curr.next = prev
            prev = curr
            curr = next_node
            if next_node is not None:
                next_node = next_node.next
        return prev
