# 1.Create a class Animal with attributes species and sound.Add a method make_sound that prints: "The [species] goes [sound]!",Instantiate objects for different animals and call make_sound.
# Define the Animal class
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    # Method to make the animal sound
    def make_sound(self):
        print(f"The {self.species} goes {self.sound}!")

# Instantiate objects for different animals
dog = Animal("dog", "woof")
cat = Animal("cat", "meow")
cow = Animal("cow", "moo")

# Call make_sound for each animal
dog.make_sound()  # Output: The dog goes woof!
cat.make_sound()  # Output: The cat goes meow!
cow.make_sound()  # Output: The cow goes moo!

# 2.Create a class Book with attributes like title, author, and year.
# Add a method that returns a description of the book.
# Create an object of Book and print out the description.
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year

    def describe(self):
        return f'the book title is{self.title},the author is{self.author}and the year is {self.year}'

book1=Book('python principles','john doe',2005)
print(book1.describe())


# 3.Define a class BankAccount with attributes owner and balance (set balance to 0 by default).Add methods deposit and withdraw to modify the balance and a method get_balance to display the balance.
# Ensure that the withdraw method does not allow the balance to go negative.
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance +=amount
            return f'{amount} deposited your balance is {self.balance}'
        else:
            return f'deposited amount less than 0'
    def withdraw(self,amount):
        if amount>self.balance:
            return f'hello {self.owner} insufficient balance to withdraw {amount}'
        else:
            self.balance-=amount
            return f'hello {self.owner} {amount} withdrawed and the new balance is {self.balance}'
    def get_balance(self):
        return f'hello {self.owner} your current blance is {self.balance}'
person1=BankAccount('farah')
person1.deposit(10000)
person1.withdraw(5000)
print(person1.get_balance())


# Define a class Rectangle with attributes width and height.
# Add methods area and perimeter to calculate the area and perimeter of the rectangle.
#  Instantiate a few rectangle objects and print their area and perimeter.
# dont do it like this
# class rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self, width, height):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)

# rectangle1 = rectangle.area(4,5)
# rectangle2=rectangle(60,7)
# rectangle3=rectangle(50,20)

# print(rectangle1.s)
# print(rectangle1.perimeter())
# print(rectangle2.area())
# print(rectangle2.perimeter())
# print(rectangle3.area())
# print(rectangle3.perimeter())

# Define the Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method to calculate the area
    def area(self):
        return self.width * self.height

    # Method to calculate the perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)

# Instantiate a few Rectangle objects
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(7, 3)
rectangle3 = Rectangle(6, 6)

# Print the area and perimeter of each rectangle
print(f"Rectangle 1: Area = {rectangle1.area()}, Perimeter = {rectangle1.perimeter()}")
print(f"Rectangle 2: Area = {rectangle2.area()}, Perimeter = {rectangle2.perimeter()}")
print(f"Rectangle 3: Area = {rectangle3.area()}, Perimeter = {rectangle3.perimeter()}")

