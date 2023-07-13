# Brute Force : O(n*l)
# def calculateMinPatforms(at, dt, n):
#     arr_sorted = zip(at, dt)
#     arr_sorted = sorted(arr_sorted, key=lambda k: k[0])
#
#     station = []
#     for i in range(0, n):
#         if len(station) == 0:
#             station.append(arr_sorted[i][1])
#         else:
#             for j in range(0, len(station)):
#                 if arr_sorted[i][0] > station[j]:
#                     station[j] = dt[i]
#                     break
#                 elif j == len(station) - 1:
#                     station.append(arr_sorted[i][1])
#     return len(station)

# Brute Force : O(nlog(n)) : Check maximum overlaps
def calculateMinPlatforms(at, dt, n):
    at.sort()
    dt.sort()

    at_idx = 0
    dt_idx = 0
    count = 0
    max_count = 0

    while at_idx < n:
        if at[at_idx] <= dt[dt_idx]:
            count += 1
            at_idx += 1
            max_count = max(max_count, count)
        else:
            count -= 1
            dt_idx += 1
    return max_count


at = [900, 910, 950, 1100, 1500, 1800]
dt = [910, 1200, 1120, 1130, 1900, 2000]
n = 6
result = calculateMinPlatforms(at, dt, n)
print(result)
