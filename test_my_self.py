# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum(numbers):
    # Initialize a variable 'total' to store the sum of numbers, starting at 0
    total = 0

    # Iterate through each element 'x' in the 'numbers' list
    for x in numbers:
        # Add the current element 'x' to the 'total'
        total += x

    # Return the final sum stored in the 'total' variable
    return total

# Print the result of calling the 'sum' function with a tuple of numbers (8, 2, 3, 0, 7)
print(sum((8, 2, 3, 0, 7)))
