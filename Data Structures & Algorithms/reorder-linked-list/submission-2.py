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
        cur = head
        if cur is None:
            return
        elif cur.next is None:
            return
        length = 1

        while cur.next is not None:
            cur = cur.next
            length+=1
        end = cur
        cur = head
        prev = None
        for i in range(math.ceil(length/2)):
            prev = cur
            cur = cur.next
        prev.next = None
        head2 = self.reverseList(cur)
        cur1 = head
        cur2 = head2

        next1 = cur1.next
        next2 = cur2.next

        for i in range(length-1):
            if i%2==0:
                cur1.next = cur2
                cur1 = next1
                if cur1 is not None:
                    next1 = cur1.next
            else:
                cur2.next = cur1
                cur2 = next2
                if cur2 is not None:
                    next2 = cur2.next
            
        return 
        
