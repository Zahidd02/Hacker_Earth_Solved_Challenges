# Brute Force : O(2n) ~ O(n)
# def searchRange(arr, x):
#     first = -1
#     last = -1
#     for i in range(0, len(arr)):
#         if arr[i] == x:
#             first = i
#             break
#     for j in range(0, len(arr)):
#         if arr[j] == x:
#             last = j
#     return [first, last]

# Optimised Approach : O(logn)
import sys


def searchRange(arr, x):
    maxNum = sys.maxsize
    minNum = -sys.maxsize
    first = binarySearchFirst(arr, 0, len(arr) - 1, x, maxNum)
    last = binarySearchLast(arr, 0, len(arr) - 1, x, minNum)

    if first == sys.maxsize:
        first = -1
    if last == -sys.maxsize:
        last = -1
    return [first, last]


def binarySearchFirst(arr, low, high, x, first):
    mid = (low + high) // 2

    if arr[mid] == x:
        first = min(first, mid)
    if low >= high:
        return first
    if x <= arr[mid]:
        return binarySearchFirst(arr, low, mid - 1, x, first)
    else:
        return binarySearchFirst(arr, mid + 1, high, x, first)


def binarySearchLast(arr, low, high, x, last):
    mid = (low + high) // 2

    if arr[mid] == x:
        last = max(last, mid)
    if low >= high:
        return last
    if x >= arr[mid]:
        return binarySearchLast(arr, mid + 1, high, x, last)
    else:
        return binarySearchLast(arr, low, mid - 1, x, last)


result = searchRange([1, 2, 4, 4, 5], 4)
print(result)

