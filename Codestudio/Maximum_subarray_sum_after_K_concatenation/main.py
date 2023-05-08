import sys

# Brute Force : O(n2)
# arr = [1, 3]
# K = 3
# newArr = []
# for x in range(0, K):
#     for y in range(0, len(arr)):
#         newArr.append(arr[y])
#
# maxSum = -sys.maxsize
# for i in range(0, len(newArr)):
#     currSum = 0
#     for j in range(i, len(newArr)):
#         currSum = currSum + newArr[j]
#         maxSum = max(maxSum, currSum)
#         if currSum < 0:
#             currSum = 0
# print(maxSum)

# Optimized approach : O(Kn)
# arr = [1, 3]
# K = 3
#
# currSum = 0
# maxSum = -sys.maxsize
# idx = 0
# for i in range(0, K * len(arr)):
#     currSum = currSum + arr[idx]
#     idx = idx + 1
#     if idx == len(arr):
#         idx = 0
#     maxSum = max(maxSum, currSum)
#     if currSum < 0:
#         currSum = 0

# Even more optimised : O(n)
# Explanation - https://www.youtube.com/watch?v=qnoOu5Usb4o
def kandanes_algo(arr):
    maxSum = -sys.maxsize
    currSum = 0
    for i in range(0, len(arr)):
        currSum = currSum + arr[i]
        maxSum = max(maxSum, currSum)
        if currSum < 0:
            currSum = 0
    return maxSum


def maxSubSumKConcat(arr, K):
    sum = 0
    for y in range(0, len(arr)):
        sum = sum + arr[y]

    if(K == 1):     # Case 1
        return kandanes_algo(arr)
    # Case 2
    elif sum < 0:   # Case 2
        for z in range(0, len(arr)):
            arr.append(arr[z])
        return kandanes_algo(arr)
    else:           # Case 3
        for z in range(0, len(arr)):
            arr.append(arr[z])
        return kandanes_algo(arr) + (K - 2) * sum


arr = [1, 3, -1, -2]  # [1, 3, -1, -2, 1, 3, -1, -2]
K = 2
result = maxSubSumKConcat(arr, K)
print(result)

