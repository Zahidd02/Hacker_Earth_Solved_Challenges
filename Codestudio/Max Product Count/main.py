from math import *


def maxProductCount(arr, n):
    dict = {}

    if n == 1:
        return [0, 0]

    for i in range(0, n):
        for j in range(i + 1, n):
            temp = arr[i] * arr[j]
            if dict.get(temp):
                dict[temp] += 1
            else:
                dict[temp] = 1

    dict = sorted(dict.items(), key=lambda t: t[1])

    min_key = dict[-1][0]
    for key, value in dict:
        if value == dict[-1][1]:
            min_key = min(min_key, key)
    anssss = [min_key for key, value in dict if min(min_key, key)]
    print(anssss)
    if dict[-1][1] == 1:
        return [0, 0]
    else:
        return [min_key, comb(dict[-1][1], 2)]  # Given the value (say 4), number of pairs of 2 that can be chosen (4C2)


result = maxProductCount([1, 2, 3, 4, 6, 8, 12, 24], 8)
print(result)
