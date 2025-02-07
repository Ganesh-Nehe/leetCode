class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}
        color_count = {} 
        result = []

        for ball, color in queries:
            if ball in ball_colors:
                old_color = ball_colors[ball]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]

            ball_colors[ball] = color
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
            
            result.append(len(color_count))

        return result