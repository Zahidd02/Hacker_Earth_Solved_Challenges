import re


class StringProblems:
    # Convert String : O(n)
    def convertString(self, str):
        n = len(str)
        new_str = ""
        for i in range(0, n):
            if i == 0 or str[i - 1] == ' ':
                new_str += str[i].upper()
            else:
                new_str += str[i]
        return new_str

    # Encode the Message
    def encode(self, message):
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
    def minimumParentheses(self, pattern):
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
    def leftRotate(self, strr, d):
        d = d % len(strr)
        rot_str = strr[0:d]
        return strr[d:] + rot_str

    # Left And Right Rotation Of A String
    def rightRotate(self, strr, d):
        d = d % len(strr)
        rot_str = strr[-d:]
        if d % len(strr) == 0:
            return rot_str
        return rot_str + strr[:len(strr) - d]

    # Longest Sub-string With K Distinct Characters
    def getLengthofLongestSubstring(self, s, k):
        i = 0
        j = 0
        max_val = 0
        n = len(s)
        while j < n:
            set_len = len(set(s[i:j + 1]))
            if set_len <= k:
                max_val = max(max_val, len(s[i:j + 1]))
                j += 1
            else:
                i += 1
                j = i
        return max_val

    # Anagram Difference
    def getMinimumAnagramDifference(self, str1, str2):
        dict = {}
        count = 0
        for item in str1:
            if dict.get(item):
                dict[item] = dict[item] + 1
            else:
                dict[item] = 1
        for item in str2:
            if not dict.get(item):
                count += 1
            elif dict[item] > 0:
                dict[item] = dict[item] - 1
        return count

    # Given a string, find the next smallest palindrome : Hard Problem
    def nextLargestPalindrome(self, s, length):
        if length % 2 == 0:
            ans = ""
            first = str(s[:length // 2])
            last = first[::-1]
            ans += first + last
            if int(ans) > int(s):
                return ans
            elif first[-1] != '9':
                ans = ""
                first = str(int(first) + 1)
                last = first[::-1]
                ans += first + last
                return ans
            else:
                ans = ""
                first = str(int(first) + 1)
                last = first[-3::-1]
                ans += first + last
                if int(ans) > int(s):
                    return ans
                else:
                    ans = ""
                    last = first[-2::-1]
                    ans += first + last
                    if int(ans) > int(s):
                        return ans
                    else:
                        ans = ""
                        first = str(int(s[:length // 2]) + 1)
                        last = first[::-1]
                        ans += first + last
                        return ans
        else:
            ans = ""
            first = str(s[:length // 2 + 1])
            last = first[-2::-1]
            ans += first + last
            if int(ans) > int(s):
                return ans
            elif first[-1] != '9':
                ans = ""
                first = str(int(first) + 1)
                last = first[-2::-1]
                ans += first + last
                return ans
            else:
                ans = ""
                first = str(int(first) + 1)
                last = first[-3::-1]
                ans += first + last
                if int(ans) > int(s):
                    return ans
                else:
                    ans = ""
                    last = first[-2::-1]
                    ans += first + last
                    return ans

    # Find K’th Character of Decrypted String : Medium Problem
    def kThCharaterOfDecryptedString(self, s, k):
        alpha_arr = re.findall('[a-z]+', s)
        num_arr = re.findall('[0-9]+', s)

        for i in range(0, len(alpha_arr)):
            temp = len(alpha_arr[i]) * int(num_arr[i])
            if k < temp:
                return alpha_arr[i][k % len(alpha_arr[i]) - 1]
            else:
                k -= temp
        return ""

    # Check if the string is in correct IP address format
    def isValidIPv4(self, ip_address):
        arr = ip_address.split('.')
        n = len(arr)
        if n < 4 or n > 4:
            return False
        for i in range(n):
            if not arr[i].isdigit() or not 0 <= int(arr[i]) <= 255:
                return False
        return True


x = StringProblems()
result = x.kThCharaterOfDecryptedString("a2b3cd3", 8)
print(result)
