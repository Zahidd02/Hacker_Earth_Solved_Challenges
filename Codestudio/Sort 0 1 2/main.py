# def sort012(arr, n) : O(2n) ~ O(n)
#
# 	# write your code here
#     # don't return anything
#     count0 = 0
#     count1 = 0
#     count2 = 0
#     for x in range(0, n):
#         if arr[x] == 0:
#             count0 = count0 + 1
#         elif arr[x] == 1:
#             count1 = count1 + 1
#         else:
#             count2 = count2 + 1
#
#     arr = []
#     for x in range(0, n):
#         if count0 > 0:
#             arr.append(0)
#             count0 = count0 - 1
#         elif count1 > 0:
#             arr.append(1)
#             count1 = count1 - 1
#         else:
#             arr.append(2)
#             count2 = count2 - 1
#     print(arr)
#
# sort012([0, 1, 2, 2, 1, 0], 6)

# Optimized Approach : O(1n) ~ O(n)
def sort012(arr):
    mid = 0
    low = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr = swap(arr, mid, low)
            mid = mid + 1
            low = low + 1

        elif arr[mid] == 2:
            arr = swap(arr, high, mid)
            high = high - 1
        else:
            mid = mid + 1

    print(arr)


def swap(arr, a, b):
    c = arr[a]
    arr[a] = arr[b]
    arr[b] = c
    return arr


sort012([0, 1, 2, 0, 1, 2])
