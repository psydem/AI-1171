import itertools

def solve_cryptarithmetic():
    # Define the letters in the equation
    letters = 'SENDMORY'
    # Define the equation
    equation = 'SEND + MORE == MONEY'

    # Generate all permutations of the digits 0-9 with the same length as the number of unique letters
    for perm in itertools.permutations('0123456789', len(letters)):
        # Create a dictionary to map letters to digits
        mapping = dict(zip(letters, perm))

        # Replace letters in the equation with corresponding digits
        translated_equation = equation.translate(str.maketrans(mapping))

        # Ensure no number starts with '0' (invalid in this puzzle)
        if any(num.startswith('0') for num in translated_equation.split() if num.isdigit()):
            continue

        # Evaluate the equation
        if eval(translated_equation):
            print("Solution found:")
            print(translated_equation)
            return mapping

    print("No solution found.")
    return None

# Example usage
solution = solve_cryptarithmetic()
if solution:
    print("Letter to digit mapping:")
    for letter, digit in solution.items():
        print(f"{letter} -> {digit}")
else:
    print("No solution exists.")
