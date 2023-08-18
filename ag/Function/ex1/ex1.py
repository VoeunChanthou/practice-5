# ex-1
# def removeMinuses(string):
#     result = ""
#     for i in range(len(string)):
#         if string[i] != "-":
#             result += string[i]
#     return result
# isContinue = True
# while isContinue:
#     text = input("Enter a word: ")
#     print(removeMinuses(text))
#     text1 = input("Do you want to continue (Y/N)?:")
#     if text1.upper() == "Y":
#         isContinue = True
#     else:
#         isContinue = False







# Ex:2
# def sum(n1, n2):
#     sumNumber = n1 + n2
#     return sumNumber
# n1 = int(input("Number 1:"))
# n2 = int(input("Number 2:"))
# print("The sum is:" + str(sum(n1, n2)))



# print(isA(text))

# ex-3
# def sum(n1, n2):
#     return n1 + n2

# numberOfTimes = int(input("Number of times:"))
# result = 0
# for i in range(numberOfTimes):
#     number = int(input("Value " + str(i + 1) + ": "))
#     if i == 0:
#         prevuisValue = number
#     else:
#         prevuisValue = sum(prevuisValue, number)
#     result = prevuisValue
# print(result)







# ex-4
# def sum(n1, n2):
#     sumNumber = 0
#     while n1 <= n2:
#         sumNumber += n1
#         n1 += 1
#     return sumNumber
# n1 = int(input("Start value: "))
# n2 = int(input("End value: "))
# print("The sum of number between " + str(n1 ) + " and " + str(n2 ) + " is: " + str(sum(n1, n2)))


# ex-4
# def sum(n1, n2):
#     return n1 + n2
# def sumFromTo(start, End):
#     total = 0
#     while start <= End:
#         total = sum(total, start)
#         start += 1
#     return total
# Numberstart = int(input("Enter Start: "))
# Numberend = int(input("Enter End: "))
# print("The sum of number between " + str(Numberstart) + " and " + str(Numberend) + " is : " + str(sumFromTo(Numberstart, Numberend)))


