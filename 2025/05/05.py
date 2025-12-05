#!/usr/bin/env python3
import sys

def parse_input():
    fresh_ranges = []
    available_ids = []
    
    # Read input from stdin
    input_data = sys.stdin.read().strip().split("\n")
    
    # Split fresh ranges and available IDs
    blank_line_index = input_data.index("")
    fresh_ranges = [tuple(map(int, line.split('-'))) for line in input_data[:blank_line_index]]
    available_ids = list(map(int, input_data[blank_line_index + 1:]))

    return fresh_ranges, available_ids

def is_fresh(ingredient_id, fresh_ranges):
    for start, end in fresh_ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def count_fresh_ingredients(fresh_ranges, available_ids):
    return sum(1 for ingredient_id in available_ids if is_fresh(ingredient_id, fresh_ranges))

def count_all_fresh_ids(fresh_ranges):
    # Merge overlapping intervals to avoid large intermediate data structures
    fresh_ranges.sort()
    merged = []

    for start, end in fresh_ranges:
        if not merged or merged[-1][1] < start - 1:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))

    # Calculate the total number of fresh IDs
    return sum(end - start + 1 for start, end in merged)

def main():
    fresh_ranges, available_ids = parse_input()
    part1_result = count_fresh_ingredients(fresh_ranges, available_ids)
    part2_result = count_all_fresh_ids(fresh_ranges)
    print(part1_result)
    print(part2_result)

if __name__ == "__main__":
    main()