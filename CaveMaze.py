################################################################################################
# Can you enter the cave?

# You are playing a video game. Your screen can be represented as a 2D array, where 0s represent
# walkable areas and 1s represent unwalkable areas. You are currently searching for the entrance
# to a cave that is located on the right side of the screen. Your character starts anywhere in
# the leftmost column. 

# Create a function that determines if you can enter the cave. You can only move left, right,
# up, or down (not allowed to move diagonally).

# To illustrate: 

# [ 
#   [0, 0, 1, 1, 1, 0, 0, 0], 
#   [0, 0, 0, 0, 1, 0, 0, 0], 
#   [0, 0, 1, 0, 0, 0, 0, 0], 
#   [0, 0, 1, 1, 1, 1, 1, 0] 
# ] 

# You found the entrance! Function should output True. 

# [ 
#   [0, 0, 0, 1, 0, 0, 0, 0], 
#   [0, 0, 0, 1, 1, 0, 0, 0], 
#   [0, 0, 0, 0, 1, 1, 0, 0], 
#   [0, 0, 0, 1, 1, 1, 1, 0] 
# ] 

# Nope, keep looking. Function should output False. 

# Examples 
#  ->   can_enter_cave([ 
#   [0, 1, 1, 1, 0, 1, 1, 0], 
#   [0, 0, 1, 1, 0, 0, 0, 0], 
#   [0, 0, 0, 0, 1, 1, 1, 0], 
#   [0, 1, 1, 1, 1, 1, 1, 0] 
# ]) -> False

# Notes 
#  ->   You are seeing the game screen from a birds-eye view. 
#  ->   Another way of thinking about it: You can enter the cave if you can move from the left
#       side of the screen to the right side by only walking up, down or right. 
#  ->   The entrance is not necessarily the first square, you may have to search for it in the
#       left hand column. 
################################################################################################
## Made by Oliver Parry
##
## 27/03/2021
################################################################################################

def can_enter_cave(cave):
  # Define constants and
  rows = len(cave)
  columns = len(cave[0])
  validPositions = []

  # Define function to append a new position to be checked
  def appendPos(row, column):
    # Append a dictionary containing the row and column
    # Note: I know a dictionary isn't needed but I think this is clearer than an array and I'm not
    # worried about performance ¯\_(ツ)_/¯
    validPositions.append({
      "row": row,
      "column": column
    })
	
  # Check all starting points
  for row in range(rows):
    if cave[row][columns - 1] == 0:
      # Add a new position to be checked
      appendPos(row, columns - 1)
	
  # Check all valid positions until there are no more
  while len(validPositions) > 0:
    pos = validPositions.pop() # Get position at the end of the array and remove it from the list
    row = pos["row"]
    column = pos["column"]
    print(cave[row][column])

    # Check if position is furthest left or in other words, the end
    if column == 0:
      return True
		
    # Set position to 2 to signify that it has already been explored
    cave[row][column] = 2

    # Check up
    if row > 0 and cave[row - 1][column] == 0:
      # Add a new position to be checked
      appendPos(row - 1, column)
    # Check down
    if row < rows - 1 and cave[row + 1][column] == 0:
      # Add a new position to be checked
      appendPos(row + 1, column)
    # Check right
    if column < columns - 1 and cave[row][column + 1] == 0:
      # Add a new position to be checked
      appendPos(row, column + 1)
    # Check left
    if column > 0 and cave[row][column - 1] == 0:
      # Add a new position to be checked
      appendPos(row, column - 1)
	
  # If you have run out of positions to search and not found the end, return False
  return False
      

# Testing                           # Should print:
print(can_enter_cave([
  [0, 1, 1, 1, 0, 1, 1, 0],
  [0, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0],
  [0, 1, 1, 1, 1, 1, 1, 0]
]))                                 # False
print(can_enter_cave([
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 0]
]))                                 # True