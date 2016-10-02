import numpy as np

# Convert a catlan number sequence to dyck path
# List => Running sum list
def catlanToDyck(catlanList):
    return np.cumsum(catlanList)

# Check whehter a sequence is a valid Calantan Sequence
# 1. For all indexes, number of 1s will always be large or equal to number of -1s
# 2. Equal number of 1s and -1s for whole sequence
# Instead of using a stack, directly using a running sum to keep track of 1s and -1s
def isValidDyckPath(catlanList):
    path = catlanToDyck(catlanList)
    for number in path:
        if number < 0: return False
    return path[-1] == 0

# Generate random list and keep checking validity until it's valid
def catlanGenerator(num):
    catlanList = [1] * num + [-1] * num
    catlanList = np.random.permutation(catlanList)
    while not isValidDyckPath(catlanList): catlanList = np.random.permutation(catlanList)
    return catlanToDyck(catlanList)
