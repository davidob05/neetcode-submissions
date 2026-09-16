"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        self.nodes = {node:Node(node.val,[])}
        self.rec_dfs(node)
        return self.nodes[node]

    def rec_dfs(self,node: Optional['Node']) -> None:
        for neighbor in node.neighbors:
            if neighbor in self.nodes:
                self.nodes[node].neighbors.append(self.nodes[neighbor])
            else:
                self.nodes[neighbor] = Node(neighbor.val, [])
                self.nodes[node].neighbors.append(self.nodes[neighbor])
                self.rec_dfs(neighbor)



        