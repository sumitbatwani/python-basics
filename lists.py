# - List -
# names = ["John", "Sarah", "Aman"]
# print(names[1:2])  # names[start: exclusion_end]

# - Largest number in a list -
# numbers = [5, 1, 2, 4, 3]
# largest_number = numbers[0]
# for item in numbers:
#     if item > largest_number:
#         largest_number = item

# print(f"largest number = {largest_number}")

# 2D List

# '''
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# '''

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for item in row:
#         print(item)

# Remove duplicate from a list
# list_of_numbers = [1, 2, 3, 4, 5, 5, 1]
# for number in list_of_numbers:
#     if list_of_numbers.count(number) > 1:
#         list_of_numbers.remove(number)
# print(list_of_numbers)

# or

# uniques = []
# for number in list_of_numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)
