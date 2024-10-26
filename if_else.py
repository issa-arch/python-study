# 1. Take three inputs from a user, separately. Print the largest of the numbers.
#  Hint: Determine what type of data is taken in as input.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
largest = max(num1, num2, num3)
print("The largest number is:", largest)

# # 2. Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,
# if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

degree=int(input('enter the temperature: '))
if degree>=30:
    print('The temperature is too high')
elif degree>=15:
    print('Normal temperature')
else:
    print('Cold')

# 3. Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print 
# "Conditions not met"
x =int(input('enter the value of x: '))
y =int(input('enter the value of y: '))
if x<=10 and x<=20 and y>10:
    print('condition met')
else:
    print('condition not met')

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access 
# granted", otherwise print "Access denied"

password ="secret123"
password=str(input('enter the password: '))
if password=='secret123':
    print('Access granted')
else:
    print('Access denied')

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is 
# greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance 
# needs improvement
score = int(input('Enter the score: '))
atten = int(input('Enter the attendance: '))
if score > 90:
    if atten > 80:
        print('Excellent student')
    else:
        print('Good score, but attendance needs improvement')
else:
    print('Good score, but attendance needs improvement')


