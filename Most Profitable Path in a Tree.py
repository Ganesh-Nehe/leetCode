from collections import deque
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Step 1: Build the adjacency list for the tree
        tree = {i: [] for i in range(len(amount))}
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Find Bob's path to the root (0) and store the time he reaches each node
        parent = {0: None}  # Used to reconstruct Bob's path
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in tree[node]:
                if neighbor not in parent:  # Avoid revisiting nodes
                    parent[neighbor] = node
                    queue.append(neighbor)

        # Reconstruct Bob's path from `bob` to `0`
        bob_path = {}
        time = 0
        node = bob
        while node is not None:
            bob_path[node] = time
            node = parent[node]
            time += 1
        
        # Step 3: Modify the `amount` array based on Bob's influence
        def dfs(node, time, profit):
            nonlocal max_profit
            # If Bob has reached this node
            if node in bob_path:
                bob_time = bob_path[node]
                if time < bob_time:
                    profit += amount[node]  # Alice gets full amount
                elif time == bob_time:
                    profit += amount[node] // 2  # Split amount with Bob
            else:
                profit += amount[node]  # Alice gets full amount

            # If it's a leaf node (only one connection that is not its parent)
            if len(tree[node]) == 1 and node != 0:
                max_profit = max(max_profit, profit)
                return

            # Explore the children (DFS)
            for neighbor in tree[node]:
                if neighbor != parent[node]:  # Avoid revisiting the parent
                    dfs(neighbor, time + 1, profit)

        # Start DFS from Alice's root (0)
        max_profit = float('-inf')
        dfs(0, 0, 0)

        return max_profit
