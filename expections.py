# try except block
try:
    age = int(input("Enter age: "))
    income = 20000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print("Age zero not allowed")
except ValueError:
    print("Invalid Value")
