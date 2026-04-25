print("Customize Your Ride")
print("1.  Bike")
print("2.  Car")

choice = int(input("Enter your choice: "))

if (choice == 1):
    print ("what type of bike do you want?")
    print("1.  Road Bike\n")
    print("2.  Mountain Bike\n")

    choice2 = int(input("Enter your choice2: "))
    if (choice2 == 1):
        print("You have chosen Road Bike")
    else :
        print("You have chosen Mountain Bike")

elif (choice == 2):
    print ("what type of car do you want?")
    print("1.  Sedan\n")
    print("2.  SUV\n")

    choice2 = int(input("Enter your choice2: "))
    if (choice2 == 1):
        print("You have chosen Sedan")
    else :
        print("You have chosen SUV")
else:
    print("Invalid choice")