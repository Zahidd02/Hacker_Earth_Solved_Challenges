# O(n) : Make a graph for the values per day. Buy if next value is greater than previous val. Sell at greater value than previous.
def getMaximumProfit(values, n):
    profit = 0
    for i in range(0, n-1):
        if values[i+1] > values[i]:
            profit += values[i+1] - values[i]
    return profit


result = getMaximumProfit([2,1,2,55], 4)
print(result)