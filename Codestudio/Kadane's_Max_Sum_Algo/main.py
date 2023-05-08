# 1. Kadane's Maximum Sum Algorithm:
# => At any given index ‘i’ of the array, we can either:
# - Append the element at index ‘i’ to the maximum sum subarray(so just add the element at index ‘i’ to the maximum
#       you’ve found so far).
# - Start a new subarray starting from index ‘i’.

import sys

arr = [1, -2, -3, 4, -1, 2, 1]
maxSum = -sys.maxsize
currSum = 0

for i in range(0, len(arr)):
    currSum = currSum + arr[i]
    maxSum = max(maxSum, currSum)
    if currSum < 0:
        currSum = 0

print(maxSum)
