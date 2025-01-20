class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        minHeap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        water_trapped = 0
        while minHeap:
            height, x, y = heapq.heappop(minHeap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    water_trapped += max(0, height - heightMap[nx][ny])
                    heapq.heappush(minHeap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        
        return water_trapped