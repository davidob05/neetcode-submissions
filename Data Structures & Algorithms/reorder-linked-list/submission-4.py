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

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        if fast is None or fast.next is None:
            return
        length = 1

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            length+=2
        if fast.next is not None:
            fast = fast.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        head2 = self.reverseList(head2)
        cur1 = head
        cur2 = head2
        

        while cur2 is not None:
            next1 = cur1.next
            next2 = cur2.next
            cur1.next = cur2
            cur2.next = next1
            cur1,cur2 = next1,next2
        return 
        
