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

# Optimized Approach :
def getProductArrayExceptSelf(arr, n):
    ans = []
    mod = 1000000000 + 7
    temp = 1
    count_zero = 0

    for i in range(0, n):
        if arr[i] != 0:
            temp = (temp * arr[i]) % mod
        else:
            count_zero = count_zero + 1

    for j in range(0, n):
        if arr[j] != 0 and count_zero == 0:
            ans.append(int(temp / arr[j]) % mod)
        elif arr[j] == 0 and count_zero == 1:
            ans.append(temp % mod)
        else:
            ans.append(0)
    return ans

result = getProductArrayExceptSelf([0, 1, 2], 3)
print(result)
