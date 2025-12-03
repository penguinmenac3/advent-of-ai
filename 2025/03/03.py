#!/usr/bin/env python3

"""
Advent of Code 2025 - Day 3: Lobby

Reads battery banks from stdin (one line per bank, digits 1-9).

Part 1: Turn on exactly 2 batteries (keeping order) to form the largest
two-digit joltage for each bank; output the sum across banks.

Part 2: Same, but turn on exactly 12 batteries to maximize the 12-digit
joltage for each bank; output the sum across banks.

Both answers are printed, one per line: part1 then part2.
"""

import sys
from typing import List


def max_subsequence_value(digits: List[int], k: int) -> int:
    """
    Return the integer value of the lexicographically largest subsequence
    of length k (stable order) using a monotonic stack. If the bank has
    fewer than k digits, use all of them.
    """
    if k <= 0 or not digits:
        return 0
    k = min(k, len(digits))

    stack: List[int] = []
    to_remove = len(digits) - k
    for d in digits:
        while stack and to_remove and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # If we didn't remove enough (digits were non-increasing), trim the end.
    stack = stack[:k]
    # Convert to int
    value = 0
    for d in stack:
        value = value * 10 + d
    return value


def parse_digits(line: str) -> List[int]:
    """Filter out non-digits to keep the solver robust to stray characters."""
    return [int(ch) for ch in line if ch.isdigit()]


def main() -> None:
    part1 = 0
    part2 = 0

    print("input > ")
    sys.stdout.flush()
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        digits = parse_digits(line)
        part1 += max_subsequence_value(digits, 2)
        part2 += max_subsequence_value(digits, 12)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
