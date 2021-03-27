################################################################################################
# Finding Patterns

# By locking at the inputs and outputs below, try to figure out the pattern and write a function
# to execute it for any number.

# Examples
#  ->   func(3456)          -> 2
#  ->   func(89265)         -> 5
#  ->   func(97)            -> 12
#  ->   func(2113)          -> -9
################################################################################################
## Made by Oliver Parry
##
## 27/03/2021
################################################################################################

# Algorithm

# Input: 97
# 9, 7
# len = 2
#
# 0 + (9 - 2) = 0 + 7 = 7
# 7 + (7 - 2) = 7 + 5 = 12
#
# Expected: 12
# Output:   12

# Input: 3456
# 3, 4, 5, 6
# len = 4
#
# 0  + (3 - 4)  = 0  + -1 = -1
# -1 + (4 - 4)  = -1 + 0  = -1
# -1 + (5 - 4)  = -1 + 1  = 0
# 0  + (6 - 4)  = 0  + 2  = 2
#
# Expected: 2
# Output:   2

def func(sequence): # Define func
    sequence = str(sequence) # Convert sequence to string so it can be iterated
    sequenceLength = len(sequence) # Save the length of string as a variable so len(num) isn't repeated later
    pattern = 0 # Create variable for sum with a default value of 0

    for num in sequence: # Iterate over each number in the sequence
        num = int(num) # Convert string to integer for calculation
        pattern += num - sequenceLength # Add (num - sequenceLength) to pattern
    
    return pattern # Return so calling the function is equivelant to pattern

# Testing                           # Should print:
print(func(2456))                   # 2
print(func(89265))                  # 5
print(func(97))                     # 12
print(func(2113))                   # -9