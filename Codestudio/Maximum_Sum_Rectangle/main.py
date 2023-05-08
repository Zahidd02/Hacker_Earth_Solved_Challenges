import sys


# Brute force : O(n6)
# def maxSumRectangle(arr, n, m):
#     coord = []
#     maxSum = -sys.maxsize
#     print("Boxes =>              [x0, x1] [y0, y1]")
#     for x0 in range(0, m):
#         for y0 in range(0, n):
#             for x1 in range(x0, m):
#                 for y1 in range(y0, n):
#                     for x in range(x0, x1 + 1):
#                         for y in range(y0, y1 + 1):
#                             print(
#                                 str(y) + " " + str(x) + " => Pointers are at " + str([x0, x1]) + " & " + str([y0, y1]))
#                             coord.append([y, x])
#                     maxSum = max(maxSum, add_coords(arr, coord))
#                     print("\n")
#                     coord = []
#     return maxSum
#
#
# def add_coords(arr, coord):
#     currSum = 0
#     for i in range(0, len(coord)):
#         currSum = currSum + arr[coord[i][0]][coord[i][1]]
#     return currSum

# Optimized Approach : O(n3)
def maxSumRectangle(arr, n, m):
    maxSum = -sys.maxsize
    for x0 in range(0, m):
        oneD_Arr = []
        for x1 in range(x0, m):
            for y in range(0, n):
                if len(oneD_Arr) < n:
                    oneD_Arr.append(arr[y][x1])
                else:
                    oneD_Arr[y] = oneD_Arr[y] + arr[y][x1]
            maxSum = max(maxSum, kadanes(oneD_Arr))
    return maxSum


def kadanes(arr):
    currSum = 0
    maxSum = -sys.maxsize
    for i in range(0, len(arr)):
        currSum = currSum + arr[i]
        maxSum = max(maxSum, currSum)
        if currSum < 0:
            currSum = 0
    return maxSum


matrix = [[17],
          [-10],
          [8],
          [-27]]

final_res = maxSumRectangle(matrix, 4, 1)
print(final_res)
