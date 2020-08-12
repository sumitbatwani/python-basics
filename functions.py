# def greet_user():
#     print("Hey User..")
#     print("Welcome aboard!")
# greet_user()

# positional arguments
def greet_user(name, surname):  # parameters
    print(f"hi {name} {surname}")


greet_user("sumit", "batwani")  # arguments

# keyword arguments (should always be after defining positional arguments)
def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")


greet(last_name="batwani", first_name="sumit")

# by default all functions return None (like null in JS)
def square(num):
    print(num * num)


print(square(3))  # returns None

# More example games/emoji_converter.py
