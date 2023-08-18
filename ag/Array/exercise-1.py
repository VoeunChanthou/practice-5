
# exercise-1
# def sum(array, number):
#     sum1 = 0
#     sum2 = 0
#     for i in range(len(array)):
#         sum1 += array[i]
#     for j in range(len(number)):
#         sum2 += number[j]
#     return str(sum1) + "\n" + str(sum2)
# array = eval(input())
# number = eval(input())
# print(sum(array, number))


# exersise-2
# def numberOfEight(array):
#     number = 0
#     for i in range(len(array)):
#         if array[i] == 8:
#             number += 1
#     if number > 0:
#         return number
#     else:
#         return "-1"
# array = eval(input())
# print(numberOfEight(array))


# exercise-3
# def arrayIndex(string):
#     for i in range(len(string)):
#         if string[i].upper() == "RADY":
#             result = i
#     return result
# index = eval(input())
# print(arrayIndex(index))


# exercise-4
# def countEven(array):
#     even = 0
#     odd = 0
#     for i in range(len(array)):
#         if array[i] %2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return "EVEN: " + str(even) + "\n" + "ODD: " + str(odd)
# array = eval(input())
# print(countEven(array))