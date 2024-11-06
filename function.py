# a function to calculate the area of triangle
def traingle_area():
    base=40
    height=70
    area=(base*height)/2
    return area
traingle_area()
def traingle_are(base,hight):
    area=(base*hight)/2
    return area
traingle_are(50,20)
# create a function that calculate the area of a rectangle
def area_rectangle():
    length=22
    width=20
    rectangle = (length*width)
    return rectangle
area_rectangle()
def area_rect(length,width):
    area=length*width
    return area
x=area_rect(20,10)
print(x)

# write a function thats going to check if a number is even or odd number
def check_even_odd(num):
    if num%2==0:
        result='even number'
    else:
        result='odd number'
        return result
value=check_even_odd(99)
print(value)

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


# Write a python program that takes from a user 5 inputs (maths, eng, swa, 
# sci, sos).
# Create a function that calculates the total marks another the average 
# marks ,then a functions that finds the grade according to the table below. 
# Use the value from total to get the average and average to find the grade.
# A > 79 , B - 60 to 79, C - 59 to 49, D - 40 to 49, E - less 40

def get_grade(marks):
    if marks >= 79:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'E'
marks = int(input('Enter the marks (0-100): '))
print(get_grade(marks))





