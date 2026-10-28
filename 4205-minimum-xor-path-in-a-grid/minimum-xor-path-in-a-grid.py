from functools import cache

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {}

        def helper(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == m - 1 and j == n - 1:
                dp[(i, j)] = {grid[i][j]}
                return dp[(i, j)]
            curr = grid[i][j]
            values = set()
            if i + 1 < m:
                for x in helper(i + 1, j):
                    values.add(curr ^ x)
            if j + 1 < n:
                for x in helper(i, j + 1):
                    values.add(curr ^ x)
            dp[(i, j)] = values
            return values
        return min(helper(0, 0))