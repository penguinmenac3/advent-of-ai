# Plan to Address Code Review Findings for `02.py`

## Goal

Improve the implementation of `02.py` to address inefficiencies and missing features identified during the code review. Specifically, focus on optimizing range processing, adding parallel processing, reducing memory usage, and improving the efficiency of pattern matching.

## Current State

- The script processes ranges sequentially and checks each number individually for validity.
- The script stores all invalid IDs in memory before summing them, leading to high memory usage for large datasets.
- The `is_invalid_id_part2` function uses a brute-force approach to check for repeating patterns, which can be computationally expensive.
- The script does not utilize parallel processing, despite the plan mentioning it as a requirement.

## Plan

1. **Optimize Range Processing**
   - Analyze the criteria for invalid IDs to identify mathematical shortcuts or patterns that allow skipping over numbers that cannot be invalid.
   - Implement these optimizations to reduce the number of numbers that need to be checked explicitly.

2. **Implement Parallel Processing**
   - Use the `multiprocessing` library to divide the workload across multiple processes.
   - Split the input ranges into chunks and assign each chunk to a separate process.
   - Aggregate the results from all processes to compute the final sums.

3. **Reduce Memory Usage**
   - ✅ Replaced the lists `invalid_ids_part1` and `invalid_ids_part2` with running sums to avoid storing all invalid IDs in memory.
   - Update the logic to directly add to the sums whenever an invalid ID is identified.

4. **Optimize Pattern Matching in `is_invalid_id_part2`**
   - Investigate more efficient algorithms for detecting repeating patterns in strings.
   - Replace the current brute-force approach with an optimized solution to reduce computational overhead.

## Acceptance Criteria

- [ ] The script processes ranges efficiently, minimizing the number of numbers checked explicitly.
- [ ] The script uses parallel processing to handle large inputs, reducing runtime significantly.
- [x] The script does not store all invalid IDs in memory, instead using running sums.
- [ ] The `is_invalid_id_part2` function uses an optimized algorithm for pattern matching.
- [ ] All changes are tested to ensure correctness and performance improvements.