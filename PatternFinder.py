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
# Method 1
# 0 + (9 - 2) = 0 + 7 = 7
# 7 + (7 - 2) = 7 + 5 = 12
#
# Method 2 [When I was eating breakfast I thought of a shorter way for this]
# (9 + 7) - 2^2 = 16 - 4 = 12
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
# Method 2
# (3 + 4 + 5 + 6) - 4^2 = 18 - 16 = 2
#
# Expected: 2
# Output:   2

def func(sequence): # Define func
    sequence = [int(num) for num in str(sequence)] # Convert sequence to array so sum() can be used (I used https://www.geeksforgeeks.org/python-convert-number-to-list-of-integers for this)
    return sum(sequence) - len(sequence)**2 # Pattern = (sum of integers) - (length of sequence^2) # I really do hate that python uses ** instead of ^, it got me stuck for a good few minutes

# Testing                           # Should print:
print(func(3456))                   # 2
print(func(89265))                  # 5
print(func(97))                     # 12
print(func(2113))                   # -9