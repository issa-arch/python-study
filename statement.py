if 20>40:
    print('20 is greater')
else:
    print("20 is less than")

# declare a variable markas then check if the markas is above 50 print pass otherwise print fail
marks=100
if marks<50:
    print('fail')
else:
    print('pass')

# declare a variable number that check if the number is even other wise print odd

num=60
if num %2==0:
    print('even')
else:
    print('odd')

# If and else and elif statement

marks=int(input('enter marks: '))
if marks>=90 and marks<=100:
    print('A')
elif marks>=80 and marks<=90:
    print('B')
elif marks>=70 and marks<=80:
    print('C')
elif marks>=60 and marks<=70:
    print('D')
elif  marks>=50 and marks<=60:
    print('E')
else:
        marks>=40 and marks<=50
        print('fail')


# write a program that takes age from input
# if age is 60 or above print you are an older
# if age is 18 and below print you are an adult
# otherwise you are a minor

age=int(input('enter your age: '))
if age>=60:
    print('you are older')
elif age>=18 and age<=60:
    print('you are adult')
else:
    print('you are minor')

# Write a program that:
# =>Takes the user's credit score and annual income as input.

credit= int(input("Enter your credit score: "))
annual = int(input("Enter your annual income: "))

# =>If the credit score is above 700, check if the income is above $50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

if credit > 700:
    if annual > 50000:
        print("Loan approved.")
    else:
        print("Income requirement not met")
else:
    print("Credit score too low")

