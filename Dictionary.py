person={
    'name':"Essa",
    'age':28,
    'gender':"male",
    'location':['kiambu',518,'nairobi'],
    'address':{
        'street':'southc',
        'city':'nairobi',
        'country':'kenya'
    }
    }

print(type(person))
print(person['name'])

# disply age
print(person['age'])

# display gender
print(person['gender'])

# diplay 518
print(person['location'][1])

# diplay nairobi
print(person['location'][2])

# diplay country
print(person['address']['country'])

# display city
print(person['address']['city'])

# update values
person['age']=40
print(person)

# add new key and a value
person['ocupation']='Doctor'
print(person)

# .keys => returns all the keys
print(person.keys())

# .values =>returns all the value in the dictionary
print(person.values())

# .items => returns a list of key and value
print(person.items())

# .pop => removes the value with the specific key
person.pop('name')
print(person)

# remove ocupation
person.pop('ocupation')
print(person)

# get() returns the value of a specific key
print(person.get('address'))