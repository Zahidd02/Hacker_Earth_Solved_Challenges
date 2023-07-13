def lengthOfLongestConsecutiveSequence(arr, n):
    sorted_arr = sorted(list(set(arr)))

    counter, maxNum = 1, 1
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == sorted_arr[i - 1] + 1:
            counter += 1
            maxNum = max(maxNum, counter)
        else:
            counter = 1

    return maxNum


result = lengthOfLongestConsecutiveSequence([33, 20, 34, 34, 30, 35], 5)
print(result)
