# Brute Force : O(n)
# def searchInsert(arr, target):
#     for i in range(0, len(arr)):
#         if arr[i] == target:
#             return i
#         elif arr[i] > target:
#             return i
#         elif i == len(arr) - 1:
#             return len(arr)
import sys

# Optimized Approach : O(logn)
pos = -1


def searchInsert(arr, target):
    global pos
    pos = len(arr)
    return binarySearch(arr, 0, len(arr) - 1, target)


def binarySearch(arr, low, high, target):
    global pos
    mid = int((low + high)/2)

    if low > high:
        return pos
    elif arr[mid] >= target:
        pos = min(pos, mid)
        return binarySearch(arr, low, mid - 1, target)
    else:
        return binarySearch(arr, mid + 1, high, target)


result = searchInsert([2, 5, 7], 6)
print(result)
