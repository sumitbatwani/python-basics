# customer = {"name": "Smith", "age": 30, "is_verified": True}
# print(customer)
# print(customer["name"])

# print(customer.get("name"))
# print(customer["Name"])  # KeyError
# print(customer.get("Name"))  # None
# print(customer.get("name", "Sumit"))
# print(customer.get("Name", "Sumit"))  # default value if key does not exists

# add new key
# customer["gender"] = "M"
# print(customer)

# convert digits to words
# digit_to_word = {
#     "0": "Zero ",
#     "1": "One ",
#     "2": "Two ",
#     "3": "Three ",
#     "4": "Four ",
#     "5": "Five ",
#     "6": "Six ",
#     "7": "Seven ",
#     "8": "Eight ",
#     "9": "Nine ",
# }
# phone_no = input("Phone: ")
# output = ""
# for digit in phone_no:
#     output = output + digit_to_word.get(digit, "!")
# print(output)

# More example emoji_converter.py
