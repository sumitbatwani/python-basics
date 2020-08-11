# Solution 1 : w/o functions
emoji_mapping = {":)": "😀", ":(": "😟"}
message = input("Enter a message: ")
message_list = message.split(" ")
output = ""
for word in message_list:
    # return same word if mapping not found
    output += emoji_mapping.get(word, word) + " "
print(output)


# Solution 2 : using resuable function
def generate_emoji(message):
    emoji_mapping = {":)": "😀", ":(": "😟"}
    message_list = message.split(" ")
    output = ""
    for word in message_list:
        # return same word if mapping not found
        output += emoji_mapping.get(word, word) + " "
    return output


message = input("Enter a message: ")
print(generate_emoji(message))
