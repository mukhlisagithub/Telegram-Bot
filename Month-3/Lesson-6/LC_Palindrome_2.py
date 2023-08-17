
# with func:
def isPalindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    print(isPalindrome(int(input("Enter a number: "))))


# with class
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[-1::-1]:
            return True
        else:
            return False

