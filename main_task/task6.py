# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.

correct_password = "admin@123"
attempts = 4
for attempt in range(attempts):
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password")
else:
    print("Account blocked")
