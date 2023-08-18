# 1.How to Remove number From a String in Python
# Input:yon12rady23him2
# output:yonradyhim

# note:you can you text[i].isnumeric() to check is number ot not

# def removeNumber(string):
#     result = ""
#     for i in range(len(string)):
#         if not string[i].isnumeric():
#             result += string[i]
#     return result
# text = input()
# print(removeNumber(text))


# exercise-2
# def avoidSpaces(string):
#     result = 0
#     for i in range(len(string)):
#         if string[i] != " ":
#             result += 1
#     return result
# text = input()
# print(avoidSpaces(text))

# exercise-3
# def upperHelf(string):
#     result = ""
#     number = len(string)/2
#     for i in range(len(string)):
#         if i >= number:
#             result += string[i].upper()
#         else:
#             result += string[i]
#     return result
# text = input()
# print(upperHelf(text))


# exercise-4
# def capitalize(string):
#     result = ""
#     for i in range(len(string)):
#         if i == 0:
#             result += string[i].upper()
#         elif i == (len(string) - 1):
#             result += string[i].upper()
#         else:
#             result += string[i]
#     return result
# text = input()
# print(capitalize(text))



# exercise-5
# def leastAndnumber(string):
#     isFound = False
#     number = 0
#     letter = 0
#     for i in range(len(string)):
#         if string[i].isnumeric():
#             number += 1
#         else:
#             letter += 1
#     if number > 0 and letter > 0:
#         isFound = True
#     return isFound
# text = input()
# print(leastAndnumber(text))



# exercise-6
# def ceckVowels(string):
#     result = "Not Accepted"
#     a = 0
#     e = 0
#     i = 0
#     o = 0
#     u = 0
#     for i in range(len(string)):
#         if string[i].upper() == "A":
#             a +=1
#         elif string[i].upper() == "E":
#             e += 1
#         elif string[i].upper() == "I":
#             i += 1
#         elif string[i].upper() == "O":
#             o += 1
#         elif string[i].upper() == "U":
#             u += 1
#     if a > 0 and e > 0 and i > 0 and o > 0 and u > 0:
#         result = "Accepted"
#     return result
# text = input()
# print(ceckVowels(text))



# exercise-7
