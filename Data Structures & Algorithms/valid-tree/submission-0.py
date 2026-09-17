class Solution:
    

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def get_root(x):
            while roots[x] != x:
                x = roots[x]
            return x
        
        if len(edges) != n - 1:
            return False

        roots = list(range(n))

        for a, b in edges:
            root_a = get_root(a)
            root_b = get_root(b)
            if root_a == root_b:
                return False
            roots[root_a] = root_b

        return True