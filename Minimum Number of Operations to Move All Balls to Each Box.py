class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        left_balls = 0
        left_ops = 0
        rb = sum(int(boxes[i]) for i in range(n))
        right_ops = sum(i * int(boxes[i]) for i in range(n))
        
        for i in range(n):
            ans[i] = left_ops + right_ops
            if boxes[i] == '1':
                left_balls += 1
                rb -= 1
            left_ops += left_balls
            right_ops -= rb
        
        return ans

        