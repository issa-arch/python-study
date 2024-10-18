fruits=['mango',[1,2,3,4,5],'banana',100,30.5,False,True]
print(type(fruits))

# Accessing elements inside a list.
# diplay banana
print(fruits[1])
# display true
print(fruits[-1])
#
print(fruits[1][4])

# Modifying elements.(replacing a character)
fruits[0]='water melon'
print(fruits)

# list methods =>used to munipulate or modify data inside a list.
# append =>used to add element at the end of a list
fruits.append("orange")
print(fruits)
fruits.append("milk")

# insert =>used items to a specific index
fruits.insert(1,1000)
print(fruits)
# insert number
fruits.insert(5,120)
print(fruits)

# remove =>used to remove thr first occurence of a specific element
num=[10,20,30,40,50,10,50]
num.remove(10)
print(num)
# remove 50
num.remove(50)
print(num)

# pop => it removes items of a specific index
num.pop(0)
print(num)

# list slicing => used to extract a subset of a data from a list
print(num[0:3])

# len ()=> it is used to get the length of a list
print(len(num))

# check if an element is inside a list
students=["issa","Ismail","ahmed","shucayb"]
print("issa" in students)

# concatenate lists
list1=[1,2,3,4,5]
list2=[6,7,8,9]
list3=list1+list2
print(list3)