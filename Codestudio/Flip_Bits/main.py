import sys

arr = [1, 0, 0, 1, 1, 1, 0]
maxSum = -sys.maxsize
currSum = 0
countZero = 0
countOne = 0

for i in range(0, len(arr)):
    if arr[i] == 0:
        countZero = countZero + 1
    else:
        countZero = countZero - 1
        countOne = countOne + 1
        if countZero < 0:
            countZero = 0
    maxSum = max(maxSum, countZero)

print(maxSum + countOne)
