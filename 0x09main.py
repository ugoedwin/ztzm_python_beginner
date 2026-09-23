correct_password = "python123"
user_input = input("Enter the password: ")

while user_input != correct_password:
    print("Incorrect password. Try again.")
    user_input = input("Enter the password:")
print("Access granted.")