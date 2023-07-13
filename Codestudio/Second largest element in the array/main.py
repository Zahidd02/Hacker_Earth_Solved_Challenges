import sys
def findSecondLargest(sequenceOfNumbers):
    large = -sys.maxsize
    second = -sys.maxsize

    for i in range(0, len(sequenceOfNumbers)):
        if sequenceOfNumbers[i] > large:
            second = large
            large = sequenceOfNumbers[i]
        elif sequenceOfNumbers[i] > second and sequenceOfNumbers[i] != large:
            second = sequenceOfNumbers[i]

    if second == -sys.maxsize:
        second = -1

    return second


result = findSecondLargest([12, 1, 35, 10, 34, 1])
print(result)