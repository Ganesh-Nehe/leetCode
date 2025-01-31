class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direc = [(0,1), (1,0), (0,-1), (-1,0)]
        island_id = 2 
        m_a = {0: 0} 

        def dfs(r, c, id):
            stack = [(r, c)]
            area = 0
            while stack:
                x, y = stack.pop()
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = id
                    area += 1
                    for dx, dy in direc:
                        stack.append((x + dx, y + dy))
            return area
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    m_a[island_id] = dfs(i, j, island_id)
                    island_id += 1
        
        max_area = max(m_a.values(), default=0)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_ids = set()
                    for dx, dy in direc:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            neighbor_ids.add(grid[ni][nj])
                    new_area = 1 + sum(m_a[id] for id in neighbor_ids)
                    max_area = max(max_area, new_area)
        
        return max_area