class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node]) 
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return False 
            
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True

        for u, v in edges:
            if u not in parent:
                parent[u] = u
                rank[u] = 0
            if v not in parent:
                parent[v] = v
                rank[v] = 0
            
            if not union(u, v): 
                return [u, v]

        return []