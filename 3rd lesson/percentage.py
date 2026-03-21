print("enter the marks of the student")
english = int(input("english: "))
french = int(input("french: "))
german = int(input("german: "))
spainish = int(input("spanish: "))
total = english + french + german + spainish
print("total marks:", total)    
percentage = (total / 400) * 100
print("percentage:", percentage)