# O(n)
def isPossible(arr, n):
    modifier = 1
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            modifier -= 1
            if modifier < 0:
                return False
            if arr[i] >= arr[i-2] or i == 1:
                arr[i-1] = arr[i]
            else:
                arr[i] = arr[i-1]
    return True


result = isPossible([62, -70, -54, -47, -10, 7, 20, 23, 39, 62], 10)
print(result)