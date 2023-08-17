# Insreasing and Desreasing String - 1370 from LeetCode

class Solution(object):
    def sortString(self, s: str) -> str:
        result = ""
        s = list()

        while s:
            smallest = min(s)
            result += smallest
            s.remove(smallest)

            for char in s:
                if char > result[-1]:
                    result += char
                    s.remove(char)
                    break

            for char in reversed(s):
                if char < result[-1]:
                    result += char
                    s.remove(char)
                    break
        return result

    s = 'aaaabbbbcccc'
    print(sortString(s))














