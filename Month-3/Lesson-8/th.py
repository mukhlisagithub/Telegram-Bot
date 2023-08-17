# class Solution(object):
#     def fizzBuzz(self, n):
#         if n % 3 == 0 and n % 5 == 0:
#             print("FizzBuzz")
#         else:
#             if n % 3 == 0:
#                 print("Fizz")
#             elif n % 5 == 0:
#                 print("Buzz")



class Solution:
    def sortString(self, s: str) -> str:
        result = []
        chars = 'abcdefghijklmnopqrstuvwxyz'
        while s:
            for c in chars:
                if c in s:
                    result.append(c)
                    s = s.replace(c,'',1)
                else:
                    chars = chars.replace(c,'')
            chars = chars[::-1]
        return ''.join(result)

    s = "aaaabbbbcccc"
    print(sortString(s))