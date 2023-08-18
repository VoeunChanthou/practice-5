# 1 - Get value from input as a string
# 2 - count how many letter that string contains
# 3 - display one letter by one letter
# 4 - check if all text is the same letter say "Okay" otherwise say "No"
# 5 - check if in string contains [ sign open and ] sign close
# 6 - check how many letter in [ ]


# step6
# text = input()
# left = ""
# right = ""
# isSeven = False
# isRange = True
# sum = 0
# for i in range(len(text)):
#     if text[i] != "[" and isRange:
#         if text[i].upper() == "X".upper():
#             result = "Okay"
#         else:
#             result = "No"
#     if text[i] == "[":
#         left += text[i]
#         isSeven = True
#         isRange = False
#     elif text[i] == "]":
#         right += text[i]
#         isSeven = False
#         isRange = True
#     elif (text[i] != "[" or text[i] != "]") and isSeven:
#         sum += 1
# if left == "[" and right == "]":
#     result = "Okay"
# else:
#     result = "No"
# print(result)
# print(sum)



# step5
# text = input()
# isSeven = False
# result = ""
# for i in range(len(text)):
#     if text[i] == "[":
#         isSeven = True
#     elif text[i] == "]":
#         isSeven = False
#     elif (text[i] != "[" or text[i] != "]") and isSeven:
#         result += text[i]
# print(result)



# step 1
# text = input()

# step2
# text = input()
# print(len(text))

#step3
# text = input()
# for i in range(len(text)):
#     print(text)

# step4
# text = input()
# isSeven = False
# for i in range(len(text)):
#     if text[0] == text[i] and not isSeven:
#         result = "Okay"
#     else:
#         result = "No"
# print(result)

