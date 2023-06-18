# Brute Force : O(n2)
def pairSum(arr, s):
    ans = []
    n = len(arr)
    arr.sort()
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == s:
                ans.append([arr[i], arr[j]])
    return ans


result = pairSum([1, 2, 3, 4, 5], 5)
print(result)