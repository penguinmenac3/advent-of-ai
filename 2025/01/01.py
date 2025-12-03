#!/usr/bin/env python3
import sys


def calculate_password_from_stream():
    """Calculates the password based on dial movements read from standard input."""
    dial_size = 100
    current_position = 50

    zero_count = 0
    zero_crossings = 0
    print("input > ")
    sys.stdout.flush()
    for line in sys.stdin:
        direction = line[0]
        steps = int(line[1:].strip())

        if direction == 'L':
            zero_crossings -= ((current_position - 1) % 100 - steps) // dial_size
            current_position = (current_position - steps) % dial_size
        elif direction == 'R':
            zero_crossings += (current_position + steps) // dial_size
            current_position = (current_position + steps) % dial_size

        if current_position == 0:
            zero_count += 1

    return zero_count, zero_crossings


if __name__ == "__main__":
    zero_count, zero_crossings = calculate_password_from_stream()
    print(zero_count)
    print(zero_crossings)
