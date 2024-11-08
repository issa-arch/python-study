# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to fin
# d the gross salary then uses  the gross salary to find the NHIF.
# To find the Kenya NHIF Rate using THIS LINK:
# Write a normal program but use functions if you feel com

basic=int(input('enter basic salary: '))
benefit=int(input('enter benefit: '))

def calculate_gross_salary(basic,benefit):
    gross_salary=basic+benefit
    return gross_salary
gross_salary=calculate_gross_salary(basic,benefit)
print('the gross salary is:',gross_salary)

def calculate_nhif(gross_salary):
    if gross_salary <= 5999:
        return 150
    elif 6000 <= gross_salary <= 7999:
        return 300
    elif 8000 <= gross_salary <= 11999:
        return 400
    elif 12000 <= gross_salary <= 14999:
        return 500
    elif 15000 <= gross_salary <= 19999:
        return 600
    elif 20000 <= gross_salary <= 24999:
        return 750
    elif 25000 <= gross_salary <= 29999:
        return 850
    elif 30000 <= gross_salary <= 34999:
        return 900
    elif 35000 <= gross_salary <= 39999:
        return 950
    elif 40000 <= gross_salary <= 44999:
        return 1000
    elif 45000 <= gross_salary <= 49999:
        return 1100
    elif 50000 <= gross_salary <= 59999:
        return 1200
    elif 60000 <= gross_salary <= 69999:
        return 1300
    elif 70000 <= gross_salary <= 79999:
        return 1400
    elif 80000 <= gross_salary <= 89999:
        return 1500
    elif 90000 <= gross_salary <= 99999:
        return 1600
    else:
        return 1700
nhif=calculate_nhif(gross_salary)
print(nhif)

def calculate_nssf(gross_salary):
    if gross_salary >= 18000:
     return 0.06 * gross_salary
nssf_contribution = calculate_nssf(gross_salary)
print("The NSSF contribution is:", nssf_contribution)