# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that
# the user would not enter any two numbers which are the same.
# Once you learn functions,revisit this and write this code inside a function.

user1=int(input('enter number1: '))
user2=int(input('enter number2: '))
user3=int(input('enter number3: '))
user4=int(input('enter number4: '))
if user1>user2 and user1>user3 and user1>user4:
    lagest=user1
elif user2>user1 and  user2>user3 and user2>user4:
    lagest=user2
elif user3>user1 and user3>user2 and user3>user4:
    lagest=user3
else:
    lagest=user4
print("the lagerst number is:",lagest)


