#Optimized Approach: O(n)
def isValidPair(arr, n, k, m):  # if (x+y) % k = m then, (x%k+y%k) % k=m therefore, (x%k) % k = (m-y%k+k) % k
    remainder = {}

    if n % 2 != 0:
        return False

    for i in range(0, n):
        mod = arr[i] % k
        if remainder.get(mod):
            remainder[mod] = remainder.get(mod) + 1
        else:
            remainder[mod] = 1

    for j in remainder.keys():
        x = (m - j + k) % k
        if remainder.get(x) and remainder[x] != remainder[j]:
            return False
    return True


result = isValidPair([1, 2, 3, 4, 5, 6], 6, 5, 2)
print(result)