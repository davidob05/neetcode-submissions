"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        nodes = {None:None}
        curr_node = head
        

        while curr_node:
            nodes[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next
        curr_node = head
        while curr_node:
            nodes[curr_node].next = nodes[curr_node.next]
            nodes[curr_node].random = nodes[curr_node.random]
            curr_node = curr_node.next
        return nodes[head]

