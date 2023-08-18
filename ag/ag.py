# 1
# text=input()
# result=""
# for i in range(len(text)):
#     if  i%2==0 and i<len(text)-1:
#         number=int(text[i])
#         for j in range(number):
#             result+=text[i+1]
#         result+="\n"
# print(result)



# 2
# text = input()
# result = ""
# isSeven = False
# for i in range(len(text)):
#     if not isSeven and text[i] != "'":
#         result += text[i]
#     elif text[i] == "'":
#         isSeven = not isSeven
# print(result)


# 3
# text = input()
# result = "No"
# i = 0
# while (i+3) < len(text):
#     if text[i].upper() + text[i+1].upper() + text[i+2].upper() + text[i+3].upper() == "RADY":
#         result = "Yes"
#     i += 1
# print(result)


# 4
# text = input()
# isSeven = False
# i = 0
# while i < len(text) and not isSeven:
#     if text[i] == "!":
#         isSeven = True
#     i += 1
# if isSeven:
#     print("True")
# else:
#     print("False")


# 5
# N = int(input())
# text = input()
# result = ""
# for i in range(N):
#     for j in range(len(text)):
#         result += text[j]
#     result += "\n"
# print(result)


# 6
# N = int(input())
# result = ""
# for i in range(N):
#     for j in range(N):
#         result += "X"
#     result += "\n"
# print(result)


# 7
# N = int(input())
# result = ""
# for i in range(N):
#     for j in range(N-i):
#         result += "X"
#     result += "\n"
# print(result)


#8
# text = input()
# result = ""
# for i in range(len(text)):
#     result += "Y"
# print(result)


# 9
# N = int(input())
# text = input()
# if text == "inside" and N >= 1 and N <= 10:
#     result = True
# elif text == "outside" and N > 10 or N < 1:
#     result = True
# else:
#     result = False
# print(result)


# 10
# text = input()
# sum = 0
# for i in range(len(text)):
#     sum += 1
# print(sum)


# 11
# text = input()
# result = ""
# isSeven = True
# for i in range(len(text)):
#     if i == 0:
#         result += text[i].upper()
#     elif not isSeven:
#         result += text[i].upper()
#         isSeven = True
#     elif text[i] == " ":
#         result += text[i]
#         isSeven = False
#     else:
#         result += text[i]
# print(result)