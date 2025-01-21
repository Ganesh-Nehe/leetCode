class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top_prefix = [0] * (n + 1)
        bottom_prefix = [0] * (n + 1)
        
        for i in range(n):
            top_prefix[i + 1] = top_prefix[i] + grid[0][i]
            bottom_prefix[i + 1] = bottom_prefix[i] + grid[1][i]

        result = float('inf')
        
        for col in range(n):
            points_top = top_prefix[n] - top_prefix[col + 1]
            points_bottom = bottom_prefix[col]
            second_robot_points = max(points_top, points_bottom)
            result = min(result, second_robot_points)
        
        return result