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

first = sys.maxsize
last = -sys.maxsize


def searchRange(arr, x):
    global first
    global last

    binarySort(arr, 0, len(arr)-1, x)

    if first == sys.maxsize:
        first = -1
    if last == -sys.maxsize:
        last = -1
    return [first, last]


def binarySort(arr, low, high, x):
    global first
    global last
    mid = int((low + high) / 2)

    if arr[mid] == x:
        first = min(first, mid)
        last = max(last, mid)
    if low >= high:
        return
    if x >= arr[mid]:
        binarySort(arr, mid + 1, high, x)
    if x <= arr[mid]:
        binarySort(arr, low, mid - 1, x)


result = searchRange([0, 1, 5, 5, 6, 7], 7)
print(result)

