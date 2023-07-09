letters = "ABCDEFG"
arr = []

# Time Complexity : O(n3)
for x in range(len(letters) - 2, -1, -1):  # Adds the full (except last element) string in reverse to original string.
    letters += letters[x]

for i in range(0, len(letters)):  # [6], [5, 6, 7], [4, 5, 6, 7, 8], ...
    for j in range(0, len(letters)):
        if not arr.__contains__(j):
            print(letters[j], end="")
        else:
            print(" ", end="")
    if len(arr) == 0:
        arr.append(len(letters) // 2)
    else:
        arr.append(arr[len(arr) - 1] + 1)
        arr.append(arr[0]-1)
        arr.sort()
        if len(arr) == len(letters):
            break
    print("")

# Output:
# ABCDEFGFEDCBA
# ABCDEF FEDCBA
# ABCDE   EDCBA
# ABCD     DCBA
# ABC       CBA
# AB         BA
# A           A