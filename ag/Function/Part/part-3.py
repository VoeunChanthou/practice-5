# exercise-1
# def countCharacter(word, char):
#     result = 0
#     for i in range(len(word)):
#         if word[i].upper() == char.upper():
#             result += 1
#     return result
# word = input()
# char = input()
# print(countCharacter(word, char))


# exercise-2
def countCharacter(word, char):
    result = 0
    for i in range(len(word)):
        if word[i].upper() == char.upper():
            result += 1
    return result
nextStep = "Y"
while nextStep == "Y":
    word = input("Enter a word: ")
    char = input("Enter character to count: ")
    print("The character " + str(char) + " occurs " + str(countCharacter(word, char)) + " Time in the word." )
    nextStep = input("Do you want to continue (Y/N)?").upper()