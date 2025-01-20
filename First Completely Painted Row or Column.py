class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        value_to_position = {}
        for r in range(m):
            for c in range(n):
                value_to_position[mat[r][c]] = (r, c)
        row_count = [0] * m
        col_count = [0] * n
        for i, value in enumerate(arr):   
            r, c = value_to_position[value]
            row_count[r] += 1
            col_count[c] += 1
            if row_count[r] == n or col_count[c] == m:
                return i
        return -1