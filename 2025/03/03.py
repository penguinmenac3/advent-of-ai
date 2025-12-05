#!/usr/bin/env python3
import sys


def main():
    part1 = 0
    part2 = 0

    print("input > ", flush=True)
    for line in sys.stdin.read().splitlines():
        if not line:
            continue
        tmp = line[:-1]
        d1 = max(tmp)
        p1 = tmp.index(d1)
        d2 = max(line[p1 + 1:])
        part1 += int(d1) * 10 + int(d2)
        
        stack = []
        to_remove = len(line) - 12
        for d in line:
            while stack and to_remove and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)
        part2 += sum(int(d) * (10 ** (12-i)) for i, d in enumerate(stack[:12]))

    print(part1, part2)


if __name__ == "__main__":
    main()
