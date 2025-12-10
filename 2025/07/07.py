#!/usr/bin/env python3
import sys
from collections import defaultdict


def count_splits(grid):
    # Only process every second row
    rows = grid[::2]

    # Initialize beam positions (start at the top row, all columns with beams)
    current_beams = defaultdict(int)
    current_beams.update({i: 1 for i, cell in enumerate(rows[0]) if cell == 'S'})
    split_count = 0

    # Process each row
    for row in rows[1:]:
        next_beams = defaultdict(int)

        for beam, value in current_beams.items():
            if value == 0:
                continue
            if row[beam] == '^':  # Splitter found
                split_count += 1
                if beam > 0:
                    next_beams[beam - 1] += value  # Left split
                if beam < len(row) - 1:
                    next_beams[beam + 1] += value # Right split
            else:
                next_beams[beam] += value  # Beam continues straight

        current_beams = next_beams

    return split_count, sum(current_beams.values())

if __name__ == "__main__":
    print("input > ", flush=True)  # Indicate input reading
    grid = [line.strip() for line in sys.stdin]
    split_count, timelines = count_splits(grid)
    print(split_count)
    print(timelines)
