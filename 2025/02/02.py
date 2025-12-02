#!/usr/bin/env python3

import sys

def main():
    """Read ranges from stdin, find invalid IDs, and print their sum."""
    ranges = sys.stdin.read().strip()

    def is_invalid_id_part1(number):
        number_str = str(number)
        length = len(number_str)
        if length % 2 == 0:
            mid = length // 2
            return number_str[:mid] == number_str[mid:]
        return False

    def is_invalid_id_part2(number):
        number_str = str(number)
        length = len(number_str)

        # Check for repeating patterns of varying lengths
        for pattern_length in range(1, length // 2 + 1):
            if length % pattern_length == 0:
                if number_str[:pattern_length] * (length // pattern_length) == number_str:
                    return True
        return False

    invalid_ids_part1_sum = 0
    invalid_ids_part2_sum = 0
    for range_str in ranges.split(","):
        start, end = map(int, range_str.split("-"))
        for number in range(start, end + 1):
            if is_invalid_id_part1(number):
                invalid_ids_part1_sum += number
            if is_invalid_id_part2(number):
                invalid_ids_part2_sum += number

    print(invalid_ids_part1_sum)
    print(invalid_ids_part2_sum)

if __name__ == "__main__":
    main()
