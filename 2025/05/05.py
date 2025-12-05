#!/usr/bin/env python3
import sys


def main():
    print("input > ", flush=True)    
    input_data = sys.stdin.read().strip().split("\n")
    blank_line_index = input_data.index("")
    fresh_ranges = [tuple(map(int, line.split('-'))) for line in input_data[:blank_line_index]]
    available_ids = list(map(int, input_data[blank_line_index + 1:]))

    part2 = 0
    fresh_ranges.sort()
    merged = []
    for start, end in fresh_ranges:
        if not merged or merged[-1][1] < start - 1:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    part2 = sum(end - start + 1 for start, end in merged)

    part1 = 0
    for ingredient_id in available_ids:
        for start, end in merged:
            if start <= ingredient_id <= end:
                part1 += 1
                break

    print(part1, part2, flush=True)


if __name__ == "__main__":
    main()
