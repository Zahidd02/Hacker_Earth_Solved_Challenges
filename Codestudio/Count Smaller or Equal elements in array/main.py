# Brute Force : O(n*m)
# def countSmallerOrEqual(a, b):
#     ans = []
#     for i in range(0, len(a)):
#         count = 0
#         for j in range(0, len(b)):
#             if a[i] >= b[j]:
#                 count = count + 1
#         ans.append(count)
#     return ans

# Optimized Approach : O(n)
finest = 0


def countSmallerOrEqual(a, b):
    global finest
    final_ans = []
    b.sort()
    for x in a:
        finest = 0
        binarySearch(b, 0, len(b) - 1, x)
        final_ans.append(finest)
    return final_ans


def binarySearch(arr, low, high, target):
    global finest
    mid = int((low + high)/2)

    if low > high:
        return finest
    if arr[mid] <= target:
        finest = max(finest, mid + 1)
        return binarySearch(arr, mid + 1, high, target)
    else:
        return binarySearch(arr, low, mid - 1, target)


result = countSmallerOrEqual([5, -1, 3, 9, 5], [9, -8, 6, 0, 9])
print(result)

