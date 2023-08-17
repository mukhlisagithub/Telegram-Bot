# Overloading: with c++
# // Online C++ compiler to run C++ program online
# #include <iostream>
# using namespace std;
#
# int sum(int x) {
#  return x;
# }
#
# int sum(int x, int y) {
#     x+y;
# }
# int main(){
#     int a,b;
#     cin>>a>>b;
#     cout<<sum(a)<<endl;
#     cout<<sum(a,b)<<endl;
#     return 0;
# }



# Overloading: with python not supported overloading in python
# def add(x):
#     return x
#
# def add(x,y):
#     return x+y
#
# print(add(4))
# print(add(4,5))

#
# def add(x,y):
#     return x+y
#
# def add(x):
#     return x
#
# def add(*y):
#     return y
#
# print(add(4))
# print(add(* 4,5))
# print(add(*7,8,9,5))



#
# a = iter('Muxlisam')
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))




# def find_added_character(string1, string2):
#     # Create a dictionary to count the frequency of each character in string1
#     char_count = {}
#     for char in string1:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#
#     # Subtract the frequency of each character in string2
#     for char in string2:
#         if char in char_count:
#             char_count[char] -= 1
#         else:
#             # If a character is not present in string1, it is the added character
#             return char
#
#     # Iterate through the dictionary and return the character with a count of 1
#     for char, count in char_count.items():
#         if count == 1:
#             return char
#
#
#
#
# string1 = "hello"
# string2 = "aaahello"
# print(find_added_character(string1, string2))  # Output: 'a'
#
#

#
# from solution import added_char
# import codewars_test as test


def find_added_character(string1, string2):
    char_count = {}
    for char in string1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return char

    for char, count in char_count():
        if count == 1:
            return char


string1 = "hello"
string2 = "aaahello"
print(find_added_character(string1, string2))  # Output: 'a'



