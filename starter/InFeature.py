# In this file, I will try the key words 'in'

# Substring function
print("win" in "I will win the game")

# Can it tell the capitalized letter? Yes
print("Win" in "I will win the game")

userPermission = [["Dan Liu","idiot"],
                  ["Clark Shen","xueba"],
                  ["Gin Guo","workholic"],
                  ["Leo Li","handsomeguy"]]

username = input("Username: ")
pwd = input("Password: ")

if [username,pwd] in userPermission:
    print("Access Grand")
else:
    print("Who are you?Spy!")