# Brute Force Approach : O(n3)
# def subArrayCount(arr, k):
#     count = 0
#     accounted = []
#     for i in range(0, len(arr)):
#         for j in range(i, len(arr)):
#             sum = 0
#             for x in range(i, j + 1):
#                 sum = sum + arr[x]
#                 if sum % k == 0 and not accounted.__contains__([i, x]):
#                     accounted.append([i, x])
#                     count = count + 1
#     return count


# Optimized Approach : O(n(n+1)/2) ~ O(n2)
# def subArrayCount(arr, k):
#     count = 0
#     for i in range(0, len(arr)):
#         sum = 0
#         for j in range(i, len(arr)):
#             sum = sum + arr[j]
#             if sum % k == 0:
#                 count = count + 1
#     return count


# Even more Optimized Approach : O(n)
# [Add remainders in a dictionary and if the remainder appears again add the last value of remainder in the answer.]
def subArrayCount(arr, k):
    count = 0
    total = 0
    remainder = {0: 1}

    for i in range(0, len(arr)):
        total = total + arr[i]
        rem = total % k
        if remainder.get(rem):
            count = count + remainder[rem]
            remainder[rem] = remainder[rem] + 1
        else:
            remainder[rem] = 1
    return count


result = subArrayCount([5, 0, 2, 3, 1], 5)
print(result)