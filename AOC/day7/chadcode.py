def can_form_y(y, x_values, current_value=0, index=0):
    """Recursive function to check if we can form y using x_values with +, *, or concatenation."""
    if current_value == y:
        return True
    if index >= len(x_values) or current_value > y:
        return False
    
    x = x_values[index]
    
    # Try addition
    if current_value + x <= y and can_form_y(y, x_values, current_value + x, index + 1):
        return True

    # Try multiplication (only if the current value is non-zero to avoid 0 * anything)
    if current_value != 0 and y % x == 0 and can_form_y(y, x_values, current_value * x, index + 1):
        return True

    # Try concatenation
    new_value = int(str(current_value) + str(x)) if current_value != 0 else x
    if new_value <= y and can_form_y(y, x_values, new_value, index + 1):
        return True

    return False

def process_file(filename):
    total_sum = 0

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(": ")
            if len(parts) != 2:
                continue
            
            try:
                y = int(parts[0])
                x_values = list(map(int, parts[1].split()))
            except ValueError:
                continue  # Skip if conversion fails

            if can_form_y(y, x_values):
                total_sum += y

    return total_sum

# Run the function
result = process_file("/home/guillaume/Documents/7331/AOC/day7/input.txt")
print("Total Sum:", result)

