string = input("Enter your own word: ")
char = input("Enter a character to find: ")
i = 0
count = 0
while i < len(string):
    if(string[i] == char):
        count += 1
    i += 1
print("The character '" + char + "' occurs " + str(count) + " times in the word '" + string + "'.")