# Brute Force : O(n)

# def search(arr, target):
#     for idx in range(0, len(arr)):
#         if arr[idx] == target:
#             return idx
#     return -1

# Optimized Approach :  O(logn)
def search(arr, low, high, target):
    mid = int((low + high) / 2)

    if arr[mid] == target:
        return mid
    elif low >= high:
        return -1
    elif target < arr[mid]:
        return search(arr, low, mid - 1, target)
    else:
        return search(arr, mid + 1, high, target)


def searchPivot(arr, low, high):
    mid = int((low + high) / 2)
    if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
        return mid
    if low >= high:
        return -1
    if arr[mid] < arr[low]:
        return searchPivot(arr, low, mid - 1)
    else:
        return searchPivot(arr, mid + 1, high)


def startFind(arr, target):
    pivot = searchPivot(arr, 0, len(arr) - 1)
    if pivot == -1:
        return search(arr, 0, len(arr) - 1, target)
    elif arr[pivot + 1] <= target <= arr[len(arr) - 1]:
        return search(arr, pivot + 1, len(arr) - 1, target)
    else:
        return search(arr, 0, pivot, target)


result = startFind([10, 11, 12, 13, 14, 15, 16, 19], 10)
print(result)
