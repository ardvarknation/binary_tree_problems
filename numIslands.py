# Solution to LeetCode "Number of Islands" problem using BFS algorithm.
# Description:
#  Given an m x n 2D binary grid, grid, which represents a map of '1's (land)
#  and '0's (water), return the number of islands.
#  An island is surrounded by water and formed by connecting adjacent lands 
#  horizontally or vertically. You may assume all four edges of grid are all
#  surrounded by water.

# Constraints:
#  - m == grid.length
#  - n == grid[0].length
#  - 1 <= m, n <= 300
#  - grid[i][j] is '0' or '1'

# Complexity: 
# O(m x n) time

from collections import deque

def numIslands(self, grid: List[List[str]]) -> int:
  # Edge case: empty grid
  if not grid:
    return 0

  rows = len(grid)
  cols = len(grid[0])
  isl_count = 0

  for r in range(rows):
    for c in range(cols):

      if grid[r][c] == "1":
        isl_count += 1

        queue = deque([(r, c)])
        grid[r][c] = "0"

        while queue:
          row, col = queue.popleft()

          directions = [
            (1, 0),    # Up
            (-1, 0),   # Down
            (0, 1),    # Right
            (0, -1)    # Left
          ]

          for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if (
              0 <= nr < rows and 
              0 <= nc < cols and
              grid[nr][nc] == "1"            
            ):
              grid[nr][nc] = "0"
              queue.append((nr, nc))

  return isl_count
