# exersies-1
# way-1
# number = input()
# sum = 0
# for i in range(len(number)):
#     sum += int(number[i])
# print(sum)

# way-2
# number = input()
# i = 0
# sum = 0
# while i < len(number):
#     sum += int(number[i])
#     i += 1
# print(sum)



# exersice-2
# way-1
# number = input()
# sum = 0
# for i in range(len(number)):
#     if number[i] != "9" and number[i] != "7":
#         sum += int(number[i])
# print(sum)

# way-2
# number = input()
# i = 0
# sum = 0
# while i < len(number):
#     if number[i] != "9" and number[i] != "7":
#         sum += int(number[i])
#     i += 1
# print(sum)



# exercise-3
# way-1
# text = input()
# sum = 0
# for i in range(len(text)):
#     if text[i] == "a" or text[i] == "A":
#         sum += 10
#     elif text[i] == "b" or text[i] == "B":
#         sum += 5
#     elif text[i] == "c" or text[i] == "C":
#         sum += 3
#     else:
#         sum += 1
# print(sum)


# way-2
# text = input()
# i = 0
# sum = 0
# while i < len(text):
#     if text[i].upper() == "A":
#         sum += 10
#     elif text[i].upper() == "B":
#         sum += 5
#     elif text[i].upper() == "C":
#         sum += 3
#     else:
#         sum += 1
#     i += 1
# print(sum)


# exersie-4
# way-1
# text = input("enter your text: ")
# number = 0
# letter = 0
# for i in range(len(text)):
#     if text[i].isnumeric() and text[i] != " ":
#         number += 1
#     elif text[i] != " ":
#         letter += 1
# print(str(letter) + " letter and " + str(number) + " number")


# way-2
# text = input("Enter your text: ")
# number = 0
# letter = 0
# i = 0
# while i < len(text):
#     if text[i].isnumeric() and text[i] != " ":
#         number += 1
#     elif text[i] != " ":
#         letter += 1
#     i += 1
# print(str(letter) + " letter and " + str(number) + " number")




# exersise-5
# text = input("Enter your text: ")
# lowercase = 0
# uppercase = 0
# for i in range(len(text)):
#     if text[i].isupper():
#         uppercase += 1
#     else:
#         lowercase += 1
# print(str(uppercase) + " uppercase and " + str(lowercase) + " lowercase")


# exercise-6
# text = input()
# i = 0
# isFalse = True
# while i < len(text) and isFalse:
#     if text[i] == "d" or text[i] == "D":
#         result = "Yes"
#     else:
#         result = "No"
#         isFalse = False
#     i += 1
# print(result)


# exercise-7
# text = input("Enter your text: ")
# i = 0
# isTrue = True
# while i < len(text) and isTrue:
#     if text[0] == text[i]:
#         result = "Yes"
#     else:
#         result = "No"
#         isTrue = False
#     i += 1
# print(result)


# exercise-8
# password1 = input()
# password2 = input()
# if password1 == password2:
#     print("Password correct!")
# else:
#     print("Password doesn't match")


# exersie-9
# text = input()
# result = ""
# isTrue = False
# for i in range(len(text)):
#     if text[i] == "#":
#         isTrue = True
#     elif isTrue:
#         for j in range(4):
#             result += text[i]
#         isTrue = False
#     else:
#         result += text[i]
# if len(result) > 0:
#     print(result)
# else:
#     print("No letter")



# exercise-10
# number = input()
# isTrue = True
# result = 0
# for i in range(len(number)):
#     if isTrue:
#         result = int(number[i])
#         isTrue = False
#     elif int(number[i]) > result:
#         result = int(number[i])
# print(result)



# exercise-11
# number = input()
# result = 0
# i = 0
# isTrue = True
# isFalse = False
# while i < len(number) and not isFalse:
#     if number[i] == "0":
#         result = int(number[i])
#         isFalse = True
#     elif isTrue:
#         result = int(number[i])
#         isTrue = False
#     elif int(number[i]) < result:
#         result = int(number[i])
#     i += 1
# print(result)




# exercise-12
# number = input()
# strign = ""
# result = 0
# isTrue = True
# for i in range(len(number)):
#     if number[i] != " ":
#         strign += number[i]
#     elif isTrue:
#         result = int(strign)
#         strign = ""
#         isTrue = False
#     elif int(strign) > result:
#         result = int(strign)
#         strign = ""
#     else:
#         strign = ""
# if int(strign) > result:
#     print(int(strign))
# else:
#     print(result)


# exercise-13 
# number = input()
# strign = ""
# result = ""
# isTrue = False
# for i in range(len(number)):
#     if number[i] != " ":
#         strign += number[i]
#         isTrue = True
#     elif isTrue:
#         if int(strign) %2 == 0:
#             result += strign + ", "
#             strign = ""
#         isTrue = False
#         strign = ""
# if int(strign) %2 == 0:
#     result += strign
#     print(result)
# else:
#     print(result[:-1])


# exercise-14
# text = input()
# result = ""
# isNum = True
# for i in range(len(text)):
#     if text[i] == "-":
#         result += text[i]
#         isNum = False
#     elif not isNum:
#         result += text[i] + ", "
#         isNum = True
# print(result[:-2])



# exercise-15
# number = input()
# result = ""
# for i in range(len(number)):
#     for j in range(int(number[i])):
#         result += "X"
#     result += "\n"
# print(result)



# exercise-16
# text = input()
# result = ""
# sum = ""
# isTrue = True
# isFalse = False
# for i in range(len(text)):
#     if text[i].isnumeric() and isTrue:
#         sum += text[i]
#         isTrue = False
#         isFalse = True
#     elif isFalse:
#         for j in range(int(sum)):
#             result += text[i]
#         result += "\n"
#         sum = ""
#         isFalse = False
#         isTrue = True
# print(result)



# exersice-17
# text = input()
# letter = ""
# number = ""
# for i in range(len(text)):
#     if text[i].isnumeric():
#         number += text[i]
#     else:
#         letter += text[i]
# print(number + letter)



# exercise-18
# text = input()
# result = ""
# for i in range(len(text)):
#     if text[i].upper() == "A":
#         result += "*"
#     elif text[i].upper() == "B":
#         result += "$"
#     else:
#         result += text[i]
# print(result)



# exercise-19
# text = input()
# odd = ""
# even = ""
# for i in range(len(text)):
#     if int(text[i]) %2 == 0:
#         even += text[i]
#     else:
#         odd += text[i]
# print(odd + even)



# exercise-20
# text = input()
# result = ""
# isTrue = False
# for i in range(len(text)):
#     if i == 0:
#         result += text[i].upper()
#     elif text[i] == " ":
#         isTrue = True
#         result += text[i]
#     elif isTrue:
#         result += text[i].upper()
#         isTrue = False
#     else:
#         result += text[i]
# print(result)