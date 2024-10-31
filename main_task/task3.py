# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.

phone_number = input("Enter your phone number: ")
if phone_number.startswith("07"):
    phone_number = "+254" + phone_number[1:]
elif phone_number.startswith("1") or phone_number.startswith("01"):
    phone_number = "+254" + phone_number
print("Formatted phone number:", phone_number)