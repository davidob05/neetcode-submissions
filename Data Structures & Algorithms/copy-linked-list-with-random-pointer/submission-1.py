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
        if not head:
            return
        nodes = {}
        nodes[head] = Node(head.val)
        queue = [head]
        while queue:
            curr = queue.pop()
            if curr.next:
                if curr.next in nodes:
                    nodes[curr].next = nodes[curr.next]
                else:
                    nodes[curr.next] = Node(curr.next.val)
                    nodes[curr].next = nodes[curr.next]
                    queue.append(curr.next)
            if curr.random:
                if curr.random in nodes:
                    nodes[curr].random = nodes[curr.random]
                else:
                    nodes[curr.random] = Node(curr.random.val)
                    nodes[curr].random = nodes[curr.random]
                    queue.append(curr.random)
        return nodes[head]

