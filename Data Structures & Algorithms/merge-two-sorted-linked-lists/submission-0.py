# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1,cur2 = list1,list2
        prev = None
        
        if cur1==None:
            return cur2
        elif cur2==None:
            return cur1
        if cur1.val<cur2.val:
            head = cur1
            cur1=cur1.next
        else:
            head = cur2
            cur2 = cur2.next
        prev = head
        while cur1 is not None or cur2 is not None:
            if cur1 is None or cur2 is None:
                prev.next = cur1 if cur2 is None else cur2
                return head


            if cur1.val<cur2.val:
                next1 = cur1.next
                prev.next = cur1
                prev = cur1
                cur1 = next1
            else:
                next2 = cur2.next
                prev.next = cur2
                prev = cur2
                cur2 = next2

            