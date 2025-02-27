class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}  # Map value to index
        n = len(arr)
        dp = {}
        max_length = 0
        
        for k in range(n):
            for j in range(k):
                x = arr[k] - arr[j]
                if x < arr[j] and x in index:  # Ensure valid Fibonacci condition
                    i = index[x]
                    dp[j, k] = dp.get((i, j), 2) + 1
                    max_length = max(max_length, dp[j, k])
        
        return max_length if max_length >= 3 else 0