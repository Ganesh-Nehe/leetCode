from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0) 
        }
        bfs_queue = deque([(0, 0, 0)])
        visited = [[False] * n for _ in range(m)]
        
        while bfs_queue:
            x, y, cost = bfs_queue.popleft()
            if x == m - 1 and y == n - 1:
                return cost
            
            if visited[x][y]:
                continue
            visited[x][y] = True
            for d in range(1, 5):
                dx, dy = directions[d]
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    new_cost = cost if grid[x][y] == d else cost + 1
                    if grid[x][y] == d:
                        bfs_queue.appendleft((nx, ny, new_cost)) 
                    else:
                        bfs_queue.append((nx, ny, new_cost)) 
        return -1