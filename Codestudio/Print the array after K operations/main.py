# O(n) : Try printing the arr each time, you will see that there are only 2 arrays as answers...
def printArrayAfterKOperations(arr, N, K):
    if K == 0:
        return arr

    largest = max(arr)
    smallest = min(arr)
    for i in range(0, N):
        arr[i] = largest - arr[i]

    if K % 2 != 0:
        return arr

    next_max = largest - smallest
    for j in range(0, N):
        arr[j] = next_max - arr[j]
    return arr


result = printArrayAfterKOperations([20, 15, 10, 5], 4, 4)
print(result)
