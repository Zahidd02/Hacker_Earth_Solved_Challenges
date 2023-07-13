# Convert String : O(n)
def convertString(str):
    n = len(str)
    new_str = ""
    for i in range(0, n):
        if i == 0 or str[i - 1] == ' ':
            new_str += str[i].upper()
        else:
            new_str += str[i]
    return new_str


# Encode the Message
def encode(message):
    new_str = ""
    message += " "
    count = 1
    for i in range(0, len(message) - 1):
        if message[i + 1] == message[i]:
            count += 1
        else:
            new_str += message[i] + str(count)
            count = 1
    return new_str


# Minimum Parentheses : O(n) : better than 96.94%
def minimumParentheses(pattern):
    count_open = 0
    count_close = 0
    for item in pattern:
        if item == "(":
            count_open += 1
        elif count_open > 0:
            count_open -= 1
        else:
            count_close += 1
    return count_open + count_close


# Left And Right Rotation Of A String
def leftRotate(strr, d):
    d = d % len(strr)
    rot_str = strr[0:d]
    return strr[d:] + rot_str


# Left And Right Rotation Of A String
def rightRotate(strr, d):
    d = d % len(strr)
    rot_str = strr[-d:]
    if d % len(strr) == 0:
        return rot_str
    return rot_str + strr[:len(strr) - d]


result = rightRotate("iksnedamwprxdhgjedhf", 22)
print(result)
