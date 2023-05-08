# Brute Force : O(n3)
# def possibleToMakeTriangle(arr):
#     for x in range(0, len(arr)):
#         for y in range(x+1, len(arr)):
#             for z in range(y+1, len(arr)):
#                 if (arr[x] + arr[y] > arr[z]) and (arr[y] + arr[z] > arr[x]) and (arr[z] + arr[x] > arr[y]):
#                     return True
#     return False

# Optimized Approach : O(n)
def possibleToMakeTriangle(arr):
    arr.sort()
    for x in range(0, len(arr) - 2):
        if arr[x] + arr[x + 1] > arr[x + 2]:
            return True
    return False


result = possibleToMakeTriangle([1, 9, 7, 4, 28])
print(result)
