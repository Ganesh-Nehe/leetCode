class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n, group = len(nums), 0
        pr = sorted([[nums[i], i] for i in range(n)], key=lambda x: x[0])
        map = [0] * n
        sets = [[n - 1, n - 1]]

        for i in range(n - 2, -1, -1):

            if pr[i + 1][0] - pr[i][0] <= limit:
                sets[-1][0] = i
            else:
                sets.append([i, i])
                group += 1

            map[pr[i][1]] = group

        for i in range(n):
            key = map[i]
            nums[i] = pr[sets[key][0]][0]
            sets[map[i]][0] += 1

        return nums