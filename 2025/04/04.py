#!/usr/bin/env python3

def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])

    def is_accessible(r, c):
        if grid[r][c] != '@':
            return False

        adjacent_positions = [
            (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
            (r, c - 1),             (r, c + 1),
            (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
        ]

        adjacent_count = 0
        for nr, nc in adjacent_positions:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                adjacent_count += 1

        return adjacent_count < 4

    accessible_count = 0
    for r in range(rows):
        for c in range(cols):
            if is_accessible(r, c):
                accessible_count += 1

    return accessible_count

def count_adjacent(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])

    adjacent_positions = [
        (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
        (r, c - 1),             (r, c + 1),
        (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
    ]

    adjacent_count = 0
    for nr, nc in adjacent_positions:
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
            adjacent_count += 1

    return adjacent_count

def count_total_removable_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])
    grid = [list(row) for row in grid]  # Convert to mutable grid

    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    if count_adjacent(grid, r, c) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'
            total_removed += 1

    return total_removed

if __name__ == "__main__":
    import sys
    print("input > ", flush=True)  # Indicate input reading
    input = sys.stdin.read
    grid = input().strip().split("\n")

    part1 = count_accessible_rolls(grid)
    part2 = count_total_removable_rolls(grid)

    print(part1)
    print(part2)