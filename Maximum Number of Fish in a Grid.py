class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # If out of bounds or land cell, return 0
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            # Collect fish and mark cell as visited by setting it to 0
            fish_count = grid[r][c]
            grid[r][c] = 0
            
            # Explore all 4 adjacent cells
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                fish_count += dfs(r + dr, c + dc)
            
            return fish_count
        
        max_fish = 0
        
        # Iterate over all cells in the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # Start DFS if the cell contains water (fish > 0)
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish