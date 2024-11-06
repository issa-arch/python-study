# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if
# they are equal to “admin@mail.com” and password is “Admin@123” , if so then print
# “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3
# tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.
mail="admin@mail.com"
passw='admin@123'
email=str(input('Your E-mail: '))
password=str(input('Your Password: '))
if email==mail:
    if password==passw:
     print('Login is Successful')
else:
    print('Invalid username or password')
