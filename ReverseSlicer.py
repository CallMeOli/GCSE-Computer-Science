################################################################################################
# Slicing Strings
 
# In this challenge you are given a string and a slice made from that string. Make a function 
# that returns an expression that can be used to make that slice. Your answer must contain 
# only the minimum number of keystrokes needed to make the slice. 
 
# Examples 
#  ->   slicer("abcd", "b")           -> [1]
#  ->   slicer("abcdefg", "cb")       -> [2:0:-1] 
#  ->   slicer("abcdefg", "be")       -> [1::3]
#  ->   slicer("abcdefgh", "bdf")     -> [1:6:2] 
 
# Notes 
#  ->   Test cases are slices that can be made with the [start : end : step] type expression.
#  ->   The strings are composed of unique characters (no repeats).
################################################################################################
## Made by Oliver Parry
##
## 20/03/2021
################################################################################################
 
def slicer(text, search): 
    # Search for a direct match
    startIndex = text.find(search)
    if startIndex >= 0: 
        if len(search) == 1:
            return "[" + str(startIndex) + "]" 
        else:
            return "[" + str(startIndex) + ":" + str(startIndex+len(search)-1) + "]" 
 
    # Get index for every letter in the search relative to what we are searching
    indexes = []
    for letter in search: 
        indexes.append(text.find(letter))
    indexesLen = len(indexes)
 
    # Pattern slice
    startIndex = indexes[0]
    endIndex = indexes[indexesLen-1]
    if indexesLen == 2:
        if endIndex > startIndex:
            return "[" + str(indexes[0]) + "::" + str(indexes[1] - indexes[0]) + "]"
        else:
            return "[" + str(startIndex) + ":" + str(endIndex-1) + ":" + str(indexes[1] - startIndex) + "]"
    elif indexesLen > 0:
        if endIndex > startIndex:
            return "[" + str(startIndex) + ":" + str(endIndex+1) + ":" + str(indexes[1] - startIndex) + "]"
        else:
            return "[" + str(startIndex) + ":" + str(endIndex-1) + ":" + str(indexes[1] - startIndex) + "]"
 
# Testing                           # Should print:
print(slicer("abcdefg", "b"))       # [1]
print(slicer("abcdefg", "cb"))      # [2:0:-1]
print(slicer("abcdefg", "be"))      # [1::3]
print(slicer("abcdefgh", "bdf"))    # [1:6:2]