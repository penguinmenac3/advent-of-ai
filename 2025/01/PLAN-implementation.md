# Plan for Implementing Dial Rotation Calculator

## Objective

Develop a Python script to calculate the number of times a dial points to zero after a series of rotations, based on streaming input directions and steps.

## Steps to Implement

1. ✅ **Define the Objective and Constraints**
   - The script should read from standard input and process each line as a rotation direction ('L' for left, 'R' for right) followed by steps.
   - Example Rotation Input: `L10` means move left by 10 steps.
   - Dial size is 100 positions.
   - Initial dial position is 50.
2. ✅ **Setup Project Structure**
   - Create a new Python script named `01.py`.
   - Ensure the script includes necessary shebang and mode settings for execution.
3. ✅ **Implement Core Logic**
   - Write a function `calculate_password_from_stream` to:
     - Initialize variables: `dial_size` to 100, `zero_count` to 0, and `current_position` to 50.
     - Loop over each line from standard input:
       - Parse direction and steps.
       - Adjust current dial position based on direction and steps.
       - Check if the current position is zero and increment `zero_count` if true.
   - Return the `zero_count`.
4. ✅ **Output the Result**
   - Implement a `main` function to call `calculate_password_from_stream` and print the resulting count of dial pointing to zero.

## Acceptance Criteria

- ✅ The script reads inputs via standard input and handles large series efficiently.
- ✅ It accurately reports the number of times the dial points to zero.
- ✅ The implementation should be robust, handling invalid inputs gracefully.
- ✅ The solution should be efficient, minimizing resource usage for large inputs.
