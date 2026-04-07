import sys
from dp import value, backtrack

def handle_input() :
    # Read input from stdin per assignment specifications and format it into a list
    input_data = sys.stdin.read().split()
    if not input_data :
        return # No input provided
    
    # The first line contains the number of characters in the alphabet
    k = int(input_data[0])
    char_vals = {} # Empty dictionary to store character values

    # The next k lines contain the character and its value
    for i in range(k) :
        char = input_data[1 + 2 * i]
        val = int(input_data[2 + 2 * i])
        char_vals[char] = val # Store the character and its value in the dictionary

    # Handling the first and second strings
    str_a = input_data[1 + (2 * k)]
    str_b = input_data[2 + (2 * k)]

    return char_vals, str_a, str_b

def main() :
    try:
        alphabet, a, b = handle_input()

        if alphabet is  None:
            return

        # Computing max value using dynamic programming
        dp_table, max_val = value(alphabet, a, b)

        # Reconstructing an optimal subsequence using backtracking
        result_str = backtrack(dp_table, alphabet, a, b)

        # Printing both max value and subsequence as per assignment specifications
        print(max_val)
        print(result_str)
    
    except Exception as e: # Error handling for invalid input
        print(f"Error processing input: {e}")

if __name__ == "__main__":
    main()