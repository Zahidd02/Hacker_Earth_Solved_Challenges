import math

# Brute Force : O(L-R)
# def sumInRanges(arr, n, queries, q):
#     ans = []
#     arrCount = 0
#     for x in range(0, n):
#         arr.append(arr[x])
#         arrCount = arrCount + arr[x]
#
#     for query in range(0, q):
#         totalSum = 0
#         for y in range(queries[query][0] - 1, queries[query][1]):
#             totalSum = totalSum + arr[y % n]
#         ans.append(totalSum)
#     return ans


# Optimized Approach : O(2n + q + n) ~ O(n)
def sumInRanges(arr, n, queries, q):
    ans = []
    prefix_arr = []
    prefix_sum = 0

    for x in range(0, 2 * n):
        prefix_sum = (prefix_sum + arr[x % n])
        prefix_arr.append(prefix_sum)

    arr_sum = prefix_arr[n - 1]

    for query in range(0, q):
        if queries[query][1] == queries[query][0]:
            ans.append(arr[(queries[query][0] - 1) % n])
            continue

        start = (queries[query][0] - 1) % n
        stop = (queries[query][1] - 1) % n
        if start >= stop:
            stop = stop + n

        if start - 1 < 0:
            total_sum = prefix_arr[stop]
        else:
            total_sum = prefix_arr[stop] - prefix_arr[start - 1]

        full_arr = (queries[query][1] - queries[query][0] - 1) // n

        total_sum = total_sum + (full_arr * arr_sum)
        ans.append(total_sum % 1000000007)
    return ans


result = sumInRanges([11, 11], 2, [[1, 2]], 1)
print(result)
