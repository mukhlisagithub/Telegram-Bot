def reorderString(s):
    result = ""
    s = list(s)

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

s = "aaaabbbbcccc"
print(reorderString(s))