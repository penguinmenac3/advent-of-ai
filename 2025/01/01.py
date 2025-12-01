#!/usr/bin/env python3
import sys


def calculate_password_from_stream():
    """
    Calculates the number of times the dial points to zero from streaming input.

    Computes the result as input is received, yielding an efficient approach to 
    immediate processing of large input series.
    
    :return: Total count of the dial pointing to zero
    """
    dial_size = 100
    zero_count = 0
    current_position = 50

    for line in sys.stdin:
        direction = line[0]
        steps = int(line[1:].strip())

        if direction == 'L':
            current_position = (current_position - steps) % dial_size
        elif direction == 'R':
            current_position = (current_position + steps) % dial_size

        if current_position == 0:
            zero_count += 1

    return zero_count


if __name__ == "__main__":
    zero_count = calculate_password_from_stream()
    print(zero_count)
