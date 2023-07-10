# Brute Force Approach : O(n(n - 1)) ~ O(n2)
# def getProductArrayExceptSelf(arr, n):
#     ans = []
#     mod = 1000000000 + 7
#     for i in range(0, n):
#         val = 1
#         for j in range(0, n):
#             if i == j:
#                 continue
#             else:
#                 val = (val * arr[j]) % mod
#         ans.append(val % mod)
#     return ans

# Optimized Approach : O(n) : O(n) space
# def getProductArrayExceptSelf(arr, n):
#     arrLR = []
#     arrRL = []
#     ans = []
#     mod = 1000000000 + 7
#
#     if n == 1:
#         return [1]
#
#     temp = 1
#     for i in range(0, n):
#         temp *= arr[i]
#         arrLR.append(temp)
#
#     temp = 1
#     for i in range(n - 1, -1, -1):
#         temp *= arr[i]
#         arrRL.insert(0, temp)
#
#     for i in range(0, n):
#         if i == 0:
#             ans.append(arrRL[1] % mod)
#         elif i == n - 1:
#             ans.append(arrLR[n - 2] % mod)
#         else:
#             ans.append((arrRL[i + 1] * arrLR[i - 1]) % mod)
#     return ans

# Optimized Space Complexity Approach : O(n) time - O(1) space, since we are not counting output array space
def getProductArrayExceptSelf(arr, n): 
    ans = []
    mod = 1000000000 + 7

    if n == 0:
        return ans
    elif n == 1:
        return [1]

    temp = 1
    for i in range(0, n):
        temp *= arr[i]
        ans.append(temp)

    prod = arr[n - 1]
    for j in range(n - 1, -1, -1):
        if j == n - 1:
            ans[n - 1] = ans[n - 2] % mod
        elif j == 0:
            ans[j] = prod % mod
        else:
            ans[j] = (prod * ans[j - 1]) % mod
            prod *= arr[j]

    return ans


result = getProductArrayExceptSelf([1, 2, 3, 4], 4)
print(result)
