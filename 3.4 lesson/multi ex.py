try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except SyntaxError:
    print("Error: Invalid syntax. Please enter two numbers separated by a comma.")

except:
    print("Error: An unexpected error occurred.")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what")