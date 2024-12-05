import copy

# Open the input file and read all lines
with open("puzzle2/input.txt") as reports:
    lines = reports.readlines()

def check_is_monotonic(arr):
    """
    Check if an array is monotonic (either entirely non-increasing or non-decreasing).
    """
    increasing, decreasing = True, True
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            decreasing = False
        elif arr[i] > arr[i + 1]:
            increasing = False
        # If neither increasing nor decreasing, it is not monotonic
        if not increasing and not decreasing:
            return False
    return True

def max_dist(arr):
    """
    Check if the absolute difference between consecutive elements is less than 4 
    and greater than 0 (strict condition for safe lines).
    """
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff >= 4 or diff == 0:
            return False
    return True

# List to store unsafe lines
unsafe_lines = []
num_safe = 0

# Process each line in the input file
for line in lines:
    # Convert the line into a list of integers
    line = list(map(int, line.strip().split()))

    # Check if the line is monotonic
    if check_is_monotonic(line):
        # If monotonic, check if it satisfies the max distance condition
        if max_dist(line):
            num_safe += 1
        else:
            unsafe_lines.append(line)
    else:
        # Non-monotonic lines are directly unsafe
        unsafe_lines.append(line)

print("safe numbers part1",num_safe)

# Try removing one element from each unsafe line to see if it can become safe
for line in unsafe_lines:
    for i in range(len(line)):
        # Create a copy of the line with one element removed
        modified_line = line[:i] + line[i+1:]

        # Check if the modified line satisfies both conditions
        if check_is_monotonic(modified_line) and max_dist(modified_line):
            num_safe += 1
            break  # No need to check further modifications for this line

# Print the number of safe lines
print("safe numbers part2",num_safe)
