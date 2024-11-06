# Write a python program that takes from a user 5 inputs (maths, eng, swa,
# sci, sos).
# Create a function that calculates the total marks another the average
# marks ,then a functions that finds the grade according to the table below.
# Use the value from total to get the average and average to find the grade.
# A > 79 , B - 60 to 79, C - 59 to 49, D - 40 to 49, E - less 40

# def get_grade(marks):
#     if marks >= 79:
#         return 'A'
#     elif marks >= 60:
#         return 'B'
#     elif marks >= 50:
#         return 'C'
#     elif marks >= 40:
#         return 'D'
#     else:
#         return 'E'
# marks = int(input('Enter the marks (0-100): '))
# print(get_grade(marks))

math=int(input('enter math: '))
eng=int(input('enter eng: '))
swa=int(input('enter swa: '))
sci=int(input('enter sci: '))
sos=int(input('enter sos: '))

def cal_total_marks(m,e,s,sc,so):
    sum=m+e+s+sc+so
    return sum
total_marks=cal_total_marks(math,eng,swa,sci,sos)
print(f'total marks is {total_marks}')

# now calculte the avarage
def calculate_average(total):
    average=total/5
    return average
avg=calculate_average(total_marks)
print(f'Average is {avg}')

def find_grade(average):
    if average>79:
        grade='A'
    elif 60<= average <=79:
        grade='B'
    elif 49<= average <=50:
        grade='C'
    elif 40<= average <=49:
        grade='D'
    else:
        grade='E'
    return grade

