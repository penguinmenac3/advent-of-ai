#!/usr/bin/env python3
import sys


def parse_row_number(line, x, width):
    while x < width and line[x] == ' ':
        x += 1
    start = x
    while x < width and line[x] != ' ':
        x += 1
    return int(line[start:x])


def parse_column_number(grid, x):
    return int("".join([
        line[x]
        for line in grid[:-1]
        if line[x] != ' '
    ]))


def part1_math(grid, x, op, width):
    result = 0 if op == '+' else 1
    for line in grid[:-1]:
        number = parse_row_number(line, x, width)
        if op == '+':
            result += number
        elif op == '*':
            result *= number
    return result


def part2_math(grid, x, op, width):
    result = 0 if op == '+' else 1
    for col in range(x, width):
        if col > x and col+1 < width and grid[-1][col+1] != ' ':
            break # Stop at the next non-space after the first
        number = parse_column_number(grid, col)
        if op == '+':
            result += number
        elif op == '*':
            result *= number
    return result


def main():
    print("input > ", flush=True)  # Indicate input reading
    lines = sys.stdin.readlines()
    grid = [line[:-1] for line in lines]
    width = len(grid[0])

    part1 = 0
    part2 = 0
    for x in range(width):
        op = grid[-1][x]
        if op == ' ':
            continue
        part1 += part1_math(grid, x, op, width)
        part2 += part2_math(grid, x, op, width)

    print(part1)
    print(part2)

# Boilerplate code for input handling
if __name__ == "__main__":
    main()
