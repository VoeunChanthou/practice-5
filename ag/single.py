# text = input()
# result = ""
# isSeven = False
# for i in range(len(text)):
#     if not isSeven and text[i] != "'":
#         result += text[i]
#     elif text[i] == "'":
#         isSeven = not isSeven
# print(result)




# WAY-2
# text = input()
# result = ""
# isSeven = False
# inRange = False
# for i in range(len(text)):
#     if isSeven and text[i] == "'":
#         inRange = False
#         isSeven = False
#     elif not isSeven and not inRange and text[i] != "'":
#         result += text[i]
#     elif text[i] == "'":
#         isSeven = True
#         inRange = True
# print(result)


# text = input()
# result = ""
# result2 = ""
# result3 = ""
# isSeven = True
# for i in range(len(text)):
#     if text[i] != "|" and isSeven:
#         result += text[i]
#     else:
#         if text[i] != "|" and not isSeven:
#             result2 += text[i]
#         else:
#             isSeven = False
# if int(result) > int(result2):
#     result3 = "The biggest number is " + str(result)
# elif int(result2) > int(result):
#     result3 = "The biggest number is " + str(result2)
# else:
#     result3 = "The number is equal"
# print(result3)


# text = input()
# result = ""
# isSeven = True
# inRange = True
# for i in range(len(text)):
#     if inRange:
#         inRange = False
#         result += text[i].upper()
#     elif text[i] == " ":
#         isSeven = False
#         result += text[i]
#     elif not isSeven:
#         result += text[i].upper()
#         isSeven = True
#     else:
#         result += text[i]
# print(result)


# text = input()
# result = ""
# isSeven = True
# isRange = False
# for i in range(len(text)):
#     if text[i] == "]":
#         isRange = True
#     elif not isSeven and not isRange:
#         if not text[i].isnumeric():
#             result += text[i]
#     elif text[i] == "[":
#         isSeven = False
#         isRange = False
# print(result)

# text = input()
# sum = 0
# for i in range(len(text)):
#     if text[i].upper() == "X":
#         sum += i
# print(sum)


# text = input()
# result = ""
# isSeven = False
# for i in range(len(text)):
#     if text[i] == "[":
#         isSeven = True
#     elif not isSeven and text[i] != "]":
#         result += text[i]
#     elif text[i] == "]":
#         isSeven = False
# print(result)


# number = int(input())
# sum = 0
# isSeven = True
# for i in range(number):
#     number1 = int(input())
#     if number1 != 7 and isSeven:
#         sum += number1
#     elif number1 == 7:
#         isSeven = False
# print(sum)


# number = int(input())
# sum = 0
# isSeven = True
# for i in range(number):
#     number1 = int(input())
#     if number1 != 7 and isSeven:
#         sum += number1
#     elif number1 == 7:
#         isSeven = False
# print("Result is:" + str(sum))



# text = input()
# result = ""
# isRange = False
# for i in range(len(text)):
#     if text[i] == "'" and not isRange:
#         isRange = True
#     elif text[i] == "'":
#         isRange = False
#     elif  isRange:
#         result += text[i]
# print(result)


# text = input()
# result = ""
# for i in range(len(text)):
#     for j in range(len(text)):
#         if j >= i and j < (len(text)- i):
#             result += text[j]
#         else:
#             result += " "
#     result += "\n"
# print(result)