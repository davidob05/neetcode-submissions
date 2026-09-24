# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        slow = head
        prev = None
        
        while cur!=None:
            if count == n:
                cur = cur.next
                prev = slow
                slow = slow.next
            else:
                cur = cur.next
                count+=1
        if prev:
            prev.next = slow.next
        else:
            head = slow.next
        return head