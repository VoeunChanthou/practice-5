# return is the keyword to return the value but not display on terminal
# print is the keyword to show/display on terminal but not return the value
# param is the parameter to pass data




# ex-1
# def numberOfUpper(word):
#     uppercase = 0
#     for i in range(len(word)):
#         if word[i].isupper():
#             uppercase += 1
#     return uppercase
# text = input("Word : ")
# print("Number of uppercase letters : " + str(numberOfUpper(text)))


# ex-2
# def getComment(grade):
#     if grade > 10:
#         return "Good"
#     else:
#         return "Bad"
# print(getComment(1+9))


# ex-3
# def getPrice(fruitName):
#     if fruitName == "banana":
#         return 2
#     elif fruitName == "apple":
#         return 5
#     elif fruitName == "orange":
#         return 1
# print("banana price is: " + str(getPrice("banana")) + " dollars")
# print("orange price is: " + str(getPrice("orange")) + " dollars")
# print("apple price is: " + str(getPrice("apple")) + " dollars")



# ex-4
# def getAbsolute(number):
#     if number < 0:
#         return -1 * number
#     else:
#         return str(number)
# print(getAbsolute(-3-2))


# ex-5
# def max(integer1, integer2):
#     if integer1 > integer2:
#         return integer1
#     else:
#         return integer2
# print("Maximum is " + str(max(2,5)))

# ex-6
# def reverseString(string):
#     result = ""
#     for i in range(len(string)):
#         result += string[len(string) - (i+1)]
#     return result
# print(reverseString("Hello PNC"))
