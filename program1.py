class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
   
        if not grid:
            return 0

        def dfs(r, c):
            # If out of bounds or at a water cell, return
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'W':
                return
            # Mark the land cell as visited by turning it into water
            grid[r][c] = 'W'
            # Explore all four possible directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'L':  # Found a new island
                    island_count += 1
                    dfs(row, col)  # Visit all connected landmasses

        return island_count

                    
        return 0
