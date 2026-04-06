import sys

def handle_input() :
    # Read input from stdin per assignment specifications and format it into a list
    lines = sys.stdin.read().splitlines()
    if not lines :
        return # No input provided
    
    # The first line contains the number of characters in the alphabet
    k = int(lines[0].strip())

    char_vals = {} # Empty dictionary to store character values
    # The next k lines contain the character and its value
    for i in range(1, k + 1) :
        char, val = lines[i].split()
        char_vals[char] = int(val) # Store the character and its value in the dictionary

    # Handling the first and second strings
    str_a = lines[k + 1].strip()
    str_b = lines[k + 2].strip()

    return char_vals, str_a, str_b

def main() :
    try:
        alphabet, a, b = handle_input()
    
    except Exception as e: # Error handling for invalid input
        print(f"Error processing input: {e}")

if __name__ == "__main__":
    main()