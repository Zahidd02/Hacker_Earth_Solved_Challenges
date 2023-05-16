def xorQuery(queries):
    arr = []
    for q in range(0, len(queries)):
        if queries[q][0] == 1:
            arr.append(queries[q][1])
        else:
            for x in range(0, len(arr)):
                arr[x] = arr[x] ^ queries[q][1]
    return arr


result = xorQuery([[2, 3], [1, 3], [2, 2]])
print(result)
