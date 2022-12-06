string = input("Eter the stuff")

# Good method:
if string == string[::-1]:
    print("palindrome thingy")

# Stupid method:
reverse = ""
for i in range(len(string), 0, -1):
    reverse += string[i-1]

if reverse == string:
    print("palindrome thingy")


# Even more stupid ERL that won't even run on a computer :)

