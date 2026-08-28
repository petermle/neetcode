from collections import deque

def numIslands(grid: list[list[str]]) -> int:
    # main idea: outer component = discover islands, bfs = marks an entire island

    # base case
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited: set[tuple] = set()
    islands = 0

    # helper function meant to fill 'visited' set
    def bfs(r, c) -> None:
        # standard queue set up for bfs
        queue = deque()
        visited.add((r, c))
        queue.append((r, c))

        while queue:
            current_row, current_col = queue.popleft()
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # left, right, up, down

            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc
                if (new_row in range(rows) and           # new_row is in grid bounds
                    new_col in range(cols) and           # new_col is in grid bounds
                    grid[new_row][new_col] == '1' and    # element/cell == island piece
                    (new_row, new_col) not in visited):  # make sure to not revisit any element/cells
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1' and (row, col) not in visited:
                bfs(row, col)
                islands += 1

    return islands

if __name__ == "__main__":
    grid = [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    result = numIslands(grid)
    print(result)
